# Badges Tools
Files for badges are able to be generated using the Badge Tools menu on the YNOproject website.

To use it, access one of the games on the site, and append `?badge_tools=true` to the url (e.g. https://ynoproject.net/2kki/?badge_tools=true).

Once there, login into an account (no need for a moderator or developer account, any account will do), go in the badges menu, and a Badge Tools option should be present at the bottom of the menu.

![The badge tool button.](/info/assets/badge_tools_button.png)

## Content of the Menu

### Badges

![The badge menu.](/info/assets/badge_general.png)
![Bottom of the badge menu.](/info/assets/badge_parameters.png)

① Entries - The different badges you are making. You can switch between entries by clicking on a badge button, and can create a new badge entry by clicking on the + button.

② Badge ID - The ID of the badge internally used by the system. The name used should be unique, tied to the condition to be easier to search, use [snake case](https://en.wikipedia.org/wiki/Snake_case), and be 30 characters or less. If the name is too generic, or could be confused with the badge of another game, don't hesitate to specify the game ID of the game in the name.

③ Game - Which game the badge should be assigned to, based on the game ID. A badge can only be assigned to one game. The ynoproject game ID is for global badges, or badges not assigned to any game in particular. When using the badge tools, by default, a badge is assigned to the game ID of the current game.

![List of games; the list may not be up to date and is only displayed as an example.](/info/assets/badge_game_id.png)

④ Group - Defines in which group the badge is. Only present for some games like ynoproject, 2kki, flow, unevendream, fog. See file for where data configured.
    - The ynoproject groups are Badges, Expeditions, Rankings, Special. Badges is for badges tied to unlocking badges, Expeditions for badges tied to expeditions, Rankings for badges tied to the rankings, and Special for everything else.
    - The 2kki groups are Exploration, Expeditions, Events & Locations, Time Trials, Challenges, End Game. Exploration is for badges tied to the world visit progress, Events & Locations for badges in general, Time Trials for badges to unlock in Time Trial Mode, Challenges for multi-conditions badges or badges to achieving specific feats, and End Game for badges tied to endings.
    - The .flow groups are Sabitsuki, Rust, Both. They should be used depending on which character can get a badge (Sabitsuki for Sabitsuki-only badges, Rust for Rust-only badges, Both for both characters).
    - The unevendream groups are Kubotsuki, Totsutsuki, Misc. They should be used depending on which character can get a badge (Totsutsuki for Totsutsuki badges, Kubotsuki for Kubotsuki badges, Misc for badges not tied to any specific character or tied to both).
    - The fog groups are Events & Locations, Leon, Tegan, Emory. Events & Locations is for badges not tied to any specific character, or to several characters at once, while Leon, Tegan and Emory are for the badges exclusive to those characters.

In case those need to be updated or edited, the groups and their names in the various languages are defined in the [groups folder](https://github.com/ynoproject/ynobadges/tree/master/lang/groups) of the ynobadges repository, while the selectable entries in the badge tools menu are defined in the [badge tools.js](https://github.com/ynoproject/forest-orb/blob/master/badgetools.js) file of the forest-orb repository.

⑤ Order - Defines in which order the badge should be displayed in the list. Left on 0 most of the time, as the badges are automatically ordered by map ID, and then by badge ID, rendering the option not needed.

⑥ Map Order - Defines in which order the badge should be displayed in the list for entries on a same map ID. Can be used to display badges in a special order if the badge ID doesn't match what you would want to be displayed.

⑦ Badge Name - Name of the badge, as submitted by the user. By default, the name set in the tools is `New Badge`: no badge should be released with this name, meaning that if you see this name, it must be fixed. In English, badge names should use [Title Case](https://en.wikipedia.org/wiki/Title_case). Unless it makes sense, text fields should use American English, and consistency on punctuation should be put: if one of those characters is used, rather than using …, —, ？, ’, “, ”, please use ..., -, ?, ', ", ". This also applies to other text fields. Do not use emojis as part of the text fields, as the shading of the UI may look off on them. The name of a badge should be unique, and not be shared or too similar to existing badges or badges waiting on the sheet.

⑧ Description - Text of the description, as submitted by the user. This field is optional and can be left empty if the badge doesn't use it. Content can be a bit free on how it is written, but proofreading, consistency, and it making sense is nonetheless required.

⑨ Condition - Text of the condition. Unlike the badge name and description, the text should be formal and clear to the user. If the condition text is made out of several sentences, each sentence should end with a dot. If it is made of only one sentence, no need for any dot. Make sure the proper vocabulary for the condition is used (proper name of the effects, collectibles, worlds), and for consistency, basing the condition text on the formatting used by existing similar badges can be done. For Time Trial badges, using `{TIME}` to define the amount of time the player has to complete the condition should be used rather than manually writing the value in the text.

⑩ Artist - Name of the artist. If there are several artists, separate them with `,` and `&` characters (e.g. `Allan, Benjamin, Chloé & Daniel`, `Estelle & Folia`). For simplicity, ideally, artists should have their name be only made of characters from the ASCII table. Make sure the name of the artist is consistent with how they are usually named for badges, and that their name isn't too close to the name of an existing artist (in which case it may need to be changed to avoid confusion).

Artists are automatically listed in the [credits](CREDITS.md) document through a script, so there should normally be no need to update it manually.

⑪ Animated - Whether a badge is animated or not.

⑫ BP - The amount of BP (Badge Points) a badge should grant. BP must be a multiple of 5 without being 5 and without being negative. If the BP are set to be 0, the badge should be set with the Hidden flag.

⑬ Requirement Type - The type of requirement the badge will need to be unlocked.
- None (Mod Granted) - The badge will not be able to be unlocked outside of being manually granted by a moderator or developer on the site.
- Tag (Default Option) - The badge will be awarded if the set condition is fullfilled.
- Multiple Tags - The badge will be awarded once all set conditions are fullfilled, or once the number of conditions to fullfill has been reached.
- Multiple Tags with Alternatives - The badge will be awarded once each set of conditions has at least one of their tags fullfilled.
- Time Trial - The badge will be awarded if the set condition is fullfilled in less time than the Required Int set.

![The various requirements.](/info/assets/badge_requirement_type.png)

⑭ Tag Requirement Count (Multiple Tags only) - Number of conditions the player has to do before unlocking the badge. If set to 1, the number of conditions the badge has will not be displayed on-screen.

![The requirements tied to Multiple Tags.](/info/assets/badge_requirement_multiple.png)

⑮ Required Int (Time Trial only) - Number of seconds the player has to obtain the badge.

![The requirements tied to Time Trial.](/info/assets/badge_requirement_time_trial.png)

⑯ Map ID - Map ID of the location that should be linked to the location displayed in the badge menu. This info is also used to order badges, so please set it even for badges where Secret Map is used. Note that it is possible to add arguments for the MapX and MapY point for a badges file, to point at a specific location point in a map, but it is not possible to set this feature through the Badge Tools menu, and requires to be manually added. In Yume 2kki, a world or part of a world may not be referenced the same way between the English and Japanese languages, not sharing the same boundary: as such, you may need to specify the exact location in some cases.

⑰ Secret - If set, before being obtained, the name of the badge will be displayed as ???, its description and condition text will not be displayed, and the art of the badge will not be displayed.

⑱ Secret Map - Do not display the location of the badge in the badge menu, to use for badges where this info should not be visible, or for badges affecting multiple locations and where this info should not be visible.

⑲ Secret Condition - If set, before being obtained, the condition text of the badge will be displayed as ???.

⑳ Hidden - If set, the badge will not appear in the badge list before being obtained, will not take part of the badge rankings, and will have a different color for the background and name in the badge list. If this is used, make sure the badge in question grants 0 BP.

㉑ Parent Badge ID - If a parent badge ID is specified, the badge will behave in a similar way than a Secret badge until the parent badge is unlocked. Must only be used for badges where you ARE forced to unlock the parent badge first (e.g. a badge for scoring 2000 points at NASU with a parent badge for scoring 1000 points in NASU makes sense, as it is impossible to get the 2000 points first. A badge for visiting a deeper world with a parent badge for visiting a badge present before it is not doable, as the player could be logged off while visiting the location of the parent badge, thus only unlocking the child badge before the parent badge).

㉒ Overlay - If a badge is set to use an overlay, several options are available.

    - Gradient - Uses the gradient of the UI theme insteads of the flat color.
    - Multiply - Uses the multiply blend mode when applying the color, can look nicer in some cases than just applying the color flat. The choice between Gradient and Multiply is usually done by testing.
    - Mask - Applies additional badge image files (suffixed with `_mask`, or `_mask_fg` and `_mask_bg` if dual is on) to only apply colors to specific areas. Mask files should be white on the areas where they are applied, and transparency is allowed. The base badge image must be grayscale.
    - Dual - Applies both foreground and background colors to the badge. Mask must be enabled to be effective.
    - Location - Overrides the user's UI theme's colors with the colors corresponding to the user's current location (color picked based on the color set for the wiki page of the world). If the current location cannot deliver a color (no wiki link/Unknown Location), the UI theme's colors will be used as a fallback.

If you check an existing badge using an overlay, you will notice the overlay parameter is just assigned to a number. This number is the result of adding the value of the parameters together, where Gradient = +1, Multiply = +2, Mask = +4, Dual = +8, and Location = +16.

![The various options available for Overlay.](/info/assets/badge_overlay.png)

㉓ Batch - Badges will not be present in the badge list for non-developers account if the selected batch has not yet been reached. For reference, batch 195 is on Friday, January 2nd, 2026 at 9PM UTC. Batch 196 is on Friday, January 9th, 2026, batch 197 on Friday, January 16th, 2026, and so on. Usually, badges are added by group of 16 for each week, but may be subject to changes depending on who can implement them, how they want to implement them, etc.

㉔ Dev - If set, the badge will not appear in the badge list and will not be able to be obtained outside of developer accounts.

㉕ Delete - Delete the selected badge.


### Condition

This section will be empty if the Requirement Type was set to None (Mod Granted).

![The options available for conditions.](/info/assets/condition_general.png)

① Entries - The different conditions you are making for a single badge. This section will not allow any option if the Requirement Type was set to a single tag. You can switch between entries by clicking on a condition button, and can create a new condition entry by clicking on the + button.

② Sub-entries -

③ Tag ID -

④ Subcondition (for multi-tag badges) -

⑤ Map ID - Map ID on which the condition takes place. If no Map ID is set, the condition file will tracked in all maps, though global triggers must be avoided whenever possible to avoid overusing and potential false positives for their trigger.

⑥ Map Coords - MapX1 Setting -1 as the value of both X/Y1 and X/Y2 will ignore said X or Y value for the check.

![The options available for the map conditions.](/info/assets/condition_map_coords.png)

⑦ Switch Condition -

- None -
- Switch -
- Switch List -
    - Switch ID -
    - Value -
    - Switch Delay - If set, the switch check will only occur if the switch was edited while the condition was tracked.
    - Additional Switch(es) -

![The options available for the switch conditions.](/info/assets/condition_switch_list.png)

⑧ Variable Condition -
- None -
- Variable -
- Variable List -
    - Variable ID -
    - Op - Check done on the value of the variable to know if the trigger should be activated or not.
        - `=` - Checks if the value of the selected variable is equal to the selected value. 
        - `<` - Checks if the value of the selected variable is less than the selected value. 
        - `>` - Checks if the value of the selected variable is greater than the selected value. 
        - `<=` - Checks if the value of the selected variable is equal or less than the selected value. 
        - `>=` - Checks if the value of the selected variable is equal or greater than the selected value. 
        - `!=` - Checks if the value of the selected variable is not equal to the selected value. 
        - `>=<` - Checks if the value of the selected variable is between the selected value 1 and the selected value 2. This option cannot be used in a Variable List condition.
    - Variable Delay - If set, the variable check will only occur if the variable was edited while the condition was tracked.
    - Variable Trigger -

Some variable IDs are not edited by the game itself, but are used by this system and can be used for triggers:
- 10000 - Amount of money the player has.
- 10001 - Amount of Max HP the first member of the party has (usually, Max HP of the protagonist, which is used as part of the drink system in some games).

![The options available for the variables.](/info/assets/condition_variable.png)
![The options available for variables in a list.](/info/assets/condition_variable_list.png)
![The options available for the variable operators.](/info/assets/condition_variable_operators.png)

⑨ Trigger -
- Default -
- Previous Map ID - Triggers the condition if the previous map the player visited corresponds to the previous map selected. The ID of the map must use 4 digits (e.g. 0009, 0011, 0123, 1640), even if the ID is less than 1000, otherwise the trigger will not work. Yume 2kki internally tracks the previous map ID in the variable 99, which can alternatively be used if a different trigger is needed, or if the game changes quickly the location between different maps which could be incorrectly reflected through this option.
- Teleport - 
- Coordinates - If set as the trigger, the Map Coords argument will automatically be set here.
- Picture - Triggers the condition if a picture with the corresponding name is displayed on-screen. Do not use this setting if the asset were to be used as part of another unrelated event in the map (e.g. asset preloading).
- Event Collision - Triggers the condition if the player enters in collision with the selected event ID. If nothing happens when entering in collision with the event (no script executed), then the trigger will not work. Several event IDs can be specified for a single condition, in which case the condition will be triggered if any of the selected events was collided. If the event is able to be interacted with to trigger the exact same action, then the badge should also be triggered as part of an Event Interaction.
- Event Interaction - Triggers the condition if the player interacts with the selected event ID. If nothing happens when interacting with the event (no script executed), then the trigger will not work. Several event IDs can be specified for a single condition, in which case the condition will be triggered if any of the selected events was interacted with.

![The options available for the trigger conditions.](/info/assets/condition_trigger.png)

⑩ Time Trial - Checks if the condition should only be triggered while in Time Trial. Time Trial badges are only supported for Yume 2kki.

⑪ Delete - Delete the selected condition.


Export - Export the generated files in a zip archive.

![The export button.](/info/assets/export_button.png)


Time Trial considerations