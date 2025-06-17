#!/usr/bin/env -S deno run --allow-read

import { object, string, boolean, number, parse, picklist, array, partial, pipe, check, checkItems, type InferInput } from "https://esm.sh/valibot@1.1.0";

const Ops = picklist(['=', '<', '>', '<=', '>=', '!=', '>=<']);

const TCondition = partial(object({
  map: number(),
  mapX1: number(),
  mapY1: number(),
  mapX2: number(),
  mapY2: number(),
  switchId: number(),
  switchValue: boolean(),
  switchIds: array(number()),
  switchValues: array(boolean()),
  switchDelay: boolean(),
  varId: number(),
  varValue: number(),
  varValue2: number(),
  varOp: Ops,
  varIds: array(number()),
  varValues: array(number()),
  varOps: array(Ops),
  varDelay: boolean(),
  varTrigger: boolean(),
  trigger: string(),
  value: string(),
  values: array(string()),
  timeTrial: boolean(),
  disabled: boolean(),
}));

const conditions = new Set<string>;
const isKnownCondition = conditions.has.bind(conditions);

const TConditions = pipe(array(string()), checkItems(isKnownCondition, 'unknown condition'));

const TBadge = partial(object({
  group: string(),
  order: number(),
  mapOrder: number(),
  bp: number(),
  reqType: string(),
  reqInt: number(),
  reqString: pipe(string(), check(isKnownCondition, 'unknown condition')),
  reqStrings: TConditions,
  reqStringArrays: array(TConditions),
  reqCount: number(),
  map: number(),
  mapX: number(),
  mapY: number(),
  secret: boolean(),
  secretMap: boolean(),
  secretCondition: boolean(),
  hidden: boolean(),
  parent: string(),
  overlayType: number(),
  art: string(),
  animated: boolean(),
  batch: number(),
  dev: boolean(),
}));

let hadError = false;
function emit(type: 'error' | 'warning' | 'notice', message: string, file?: string, line?: number) {
  // GitHub Actions annotation format
  let annotation = `::${type}`;
  if (file) {
    annotation += ` file=${file}`;
    if (line !== undefined) annotation += `,line=${line + 1}`; // 1-based for GitHub
  }
  annotation += `::${message}`;
  console.log(annotation);
  if (type === 'error') hadError = true;
}

if (import.meta.main) (async function() {
  const root = new URL('..', import.meta.url).pathname;
  const join = (...parts: string[]) => parts.join('/');

  // 1. Load and validate all conditions
  const conditionsDir = join(root, 'conditions');
  const conditionGames: string[] = [];
  for await (const gameEntry of Deno.readDir(conditionsDir)) {
    if (gameEntry.isDirectory) conditionGames.push(gameEntry.name as string);
  }
  await Promise.all(conditionGames.map(async (game) => {
    const gameDir = join(conditionsDir, game);
    for await (const fileEntry of Deno.readDir(gameDir)) {
      if (!fileEntry.isFile || !fileEntry.name.endsWith('.json')) continue;
      const name = fileEntry.name.replace(/\.json$/, '');
      try {
        const data = JSON.parse(await Deno.readTextFile(join(gameDir, fileEntry.name)));
        parse(TCondition, data);
      } catch (e) {
        emit('error', e.message || e, join('conditions', game, fileEntry.name));
      }
      // Always add the condition name, even if parse fails
      conditions.add(name);
    }
  }));

  // 2. Load and validate all badges
  const badgesDir = join(root, 'badges');
  const badgeGames: string[] = [];
  for await (const gameEntry of Deno.readDir(badgesDir)) {
    if (gameEntry.isDirectory) badgeGames.push(gameEntry.name as string);
  }
  const badges: any[] = [];
  const badgeNames = new Set<string>();
  await Promise.all(badgeGames.map(async (game) => {
    const gameDir = join(badgesDir, game);
    for await (const fileEntry of Deno.readDir(gameDir)) {
      if (!fileEntry.isFile || !fileEntry.name.endsWith('.json')) continue;
      const name = fileEntry.name.replace(/\.json$/, '');
      try {
        const data = JSON.parse(await Deno.readTextFile(join(gameDir, fileEntry.name)));
        const badge = parse(TBadge, data);
        badges.push({ ...badge, __name: name, __file: join('badges', game, fileEntry.name) });
        badgeNames.add(name);
      } catch (e) {
        emit('error', e.message || e, join('badges', game, fileEntry.name));
      }
    }
  }));

  // 3. Validate badge parent references
  for (const badge of badges) {
    if (badge.parent && !badgeNames.has(badge.parent)) {
      emit('error', `parent '${badge.parent}' does not exist`, badge.__file);
    }
  }
  if (hadError) {
    Deno.exit(1);
  }
})();
