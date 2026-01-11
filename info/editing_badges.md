# Editing Badges

In some cases, you may need to edit the property of existing badges, whether it is to edit a condition, update the art, or remove it.


## Finding a Badge ID and Its Associated Data

1. Open a lang file. Any will do, but using the [English one](https://github.com/ynoproject/ynobadges/blob/master/lang/en.json) should be easier.
2. Use CTRL + F, and enter either the name of the badge, or an identifying element for it (e.g. condition or description).
3. Once you found the badge, copy its badge ID.

From there, you can find the badges, conditions and images files of the badge:
- By going at `https://github.com/ynoproject/ynobadges/blob/master/badges/`, and appending to it the game ID, the badge ID and the .json extension, you should find its badge file (e.g. for the Mermaid badge of Uneven Dream, `https://github.com/ynoproject/ynobadges/blob/master/badges/unevendream/seriri.json`, as `unevendream` is the game ID of Uneven Dream and `seriri` is the badge ID of said badge).
- The badges file should list you the conditions file(s) used by said badge. By going at `https://github.com/ynoproject/ynobadges/blob/master/conditions/`, and appending to it the game ID, the condition ID and the .json extension, you should be able to find the condition files (e.g. for the Mermaid badge of Uneven Dream, `https://github.com/ynoproject/ynobadges/blob/master/conditions/unevendream/mermaid_effect_chamber.json`, as `unevendream` is the game ID of Uneven Dream and `mermaid_effect_chamber` is the condition ID of said badge).
- By going at `https://github.com/ynoproject/ynobadges/blob/master/images/`, and appending to it the badge ID and the .png extension, you should find its static art. If the badges file listed the badge as being animated, then by replacing .png by .gif, you should also find the animated art of the badge.

You can edit the data of those files directly to adjust their properties, adjust the condition, etc.: I will not go into those specific details as it really depends on the case, so I will focus on more global cases.


## Adding Triggers to an Existing Badge

You may need to add triggers to an existing badge, either because more triggers were requested to be added, or because the game was edited, requiring the badge to be edited to make more sense.

1. Go in the badges file of your badge.
2. Change the reqType from tag (if currently tag) to tags, or to tagArrays depending on the case: you can check the files `https://github.com/ynoproject/ynobadges/blob/master/badges/2kki/01.json` and `https://github.com/ynoproject/ynobadges/blob/master/badges/flow/smile_bathtub.json` as references for those. Add a reqCount if needed.
3. Make sure you don't remove the current trigger if it should stay, and add new conditions IDs to the file.
4. Create those conditions IDs and add their data.
5. If the conditions text needs to be adjusted, adjust it in each language, and adjust its strikethrough properties if it also needs to be edited.


## Replacement of an Existing Badge

1. If the artist needs to be changed, edit the artist property in the badges file.
2. If the new art is animated while the old art wasn't, add the animated property to the badge.
3. If the new art is not animated while the old art was, remove the animated property of the badge, and delete the animation file.
4. Update the art of the badge.
5. Replace the name and description of the badge.


## Replacement of a Removed Badge

Those badges should be listed on the sheet as linked to a pull request, which was the one that removed the badges. Unless specifically requested, the data of those badges should be made out of the badge name, description, artist name and art of the new entry, while all the other properties should be reused from the removed badge.

Reusing the same name for the badge ID and conditions ID allow users that already collected the badge in the past to automatically unlock it, as its unlock data is still stored in the database.

1. Using the badge tools, generate data for the badge.
2. Reuse the data present in the pull request that removed them, that is, the badge ID and its properties, the conditions ID and its properties, the condition text.
3. Adjust the badge name, description, artist name and animation property based on what the new entry indicates.
4. After badge export, don't forget to add the files for the art, matching with the badge ID.
5. Reuse and reapply the conditions text that has been used in the different lang files.


## Removing a Badge

1. Delete the badges, conditions and images files of the badge.
2. In each lang file, delete the entry of the badge. You can quickly go to it by doing CTRL + F in each file.

In some cases, the conditions files may be used by other badges as well: if it is the case, keep those conditions files as they are still in use. Knowing whether a conditions file is still in use can be a bit hard without manually checking, but the GitHub pull request check should normally inform you if a check fails due to a lack of conditions file, which should be able to be used for the purpose of knowing that.