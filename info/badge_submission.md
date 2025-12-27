# Badge Submission

## Submitting a Badge

Badges can be submitted through two different ways, either through the [badge proposal Google Forms](https://forms.gle/tWJNdG8pTS1vNtGb8), or through the badge-proposals channel of the [YNOproject Discord](https://ynoproject.net/discord), the former requiring a Google account, the latter a Discord account.

Once submitted, a badge will be added to the [Badge Proposals Spreadsheet](https://docs.google.com/spreadsheets/d/10xqJbYKHPhSdk9NRfWim9fZvfHSdvNfNTPopHnFlt18/). Badges submitted through the form will go on the Form_Submissions page, waiting for a sheet handler to check the entry, and will later be moved to Reservations (if a reservation, and if the reservation is valid), to Waiting_Sheet (if a submission, and the submission is valid), or to the Badge_Mausoleum (if the entry is invalid/cannot be accepted), following a comment explaining the reason it could not be accepted (the entry will stay on Form_Submissions with the rejection reason for a few days as to make it easier to see). 

If a badge is submitted through Discord, a sheet handler will take care of directly putting the entry on the Reservations or Waiting_Sheet page, depending on the entry.

Reservations have 3 months to be made, after which they are moved to the Badge_Mausoleum if left untouched, or be reused by someone else.

Entries on the Waiting_Sheet will be added to the site one of the next Fridays after its addition, depending on availability and how many entries are waiting.

## Rules

Before submitting a badge, please consider the following points:
- Please read the [Badge Rules Document], and take it into consideration.
- Take into account the various clauses and points mentioned thorough this document.
- Check if there is not already a badge for it in the game.
- Check if it may not be too close with an existing badge in the game, or if the area in question is not already crowded by badges.
- Check whether it is conflicting with an existing badge present on the Badge Proposals Spreadsheet, by doing CTRL + F as to search whether a badge already exists on the Reservations, Waiting_Sheet, Form_Submissions, Badge_Portal, and Impossiblium pages: if it is too close or conflicts with an entry present on one those pages, the entry will not be able to be accepted. 
- Think whether it makes sense to have a badge for doing what you request.
- If the badge is for a new game, or content added in a new update, make sure you respect the submission time. Entries for new Yume 2kki update content cannot be reserved less than 3 days after, and major content updates of other games as well as new releases cannot be reserved less than 7 days after.
- Think whether or not the badge wanted is trackable. As part of the badge system, we are able to know the following elements:
    - Current map
    - Current coordinate/current set of coordinates of the player
    - Status of a switch (tracking several switches at once as part of a single trigger may be unreliable)
    - Status of a variable (tracking several variables at once as part of a single trigger may be unreliable)
    - Previous map
    - Display of a specific picture on-screen (may not be trackable if the game calls the picture as part of preloading, which is sometimes done in Yume 2kki)
    - Interaction with an event (e.g. NPC; not trackable if interacting doesn't do anything)
    - Collision with an event (e.g. NPC; not trackable if colliding doesn't do anything)

Several of these triggers can be combined as part of a badge, and several conditions can be used.

Anything else that was not mentioned as part of these triggers is untrackable. As such, tracking whether a specific NPC is on-screen is not possible, unless the NPC has a limited coordinates set. Additionally, as collecting effects (items) and skills is not directly trackable, unless the game tracks it itself through switches and/or variables, having badges for obtaining them will be impossible in those games (affects Answered Prayers, nostAlgic, FOG). Tracking arbitrary values (e.g. playtime, how much time the player has been on a map...) is also untrackable unless the game tracks it itself.

- If you want to do a badge that would be tracked independently of the map, this requires to be asked in advance.


## Author Clauses

Authors can add clauses for submitting badges for their content. None exist at the moment for the games on the site, but this section could be updated if requested.


### General

- Areas that are planned to be removed, heavily reworked, or implied to be a work-in-progress area in a game are closed too, due to being planned to stay only for a small amount of time or due to having to change completely the condition, art or internal trigger later.


## Submission Fields

All of those elements are requested when submitting a badge. If submitting through the sheet, those elements will already be highlighted. Otherwise, if submitting through Discord, you will need to write about them.

- **Badge Name**: The name of your badge. It must be unique, and not be already used by an existing badge, or conflicting with an existing entry on the sheet. The name will be used with title case (e.g. "badge lover" would be "Badge Lover"). If submitting a reservation and that you are not yet sure on the name, write "TBD" (To be determined) instead. Do not use emojis as to not mess up the text shading.
- **Target Game**: Game of the badge. If using the form, and that a new game allows for badges to be submitted, but is not yet present on the list, use N/A instead.
- **Submitted by**: Name of the author of the badge. If the badge was made by several authors, write the name of all of its authors.
- **Description (optional)**: Description of the badge. Do not use emojis as to not mess up the text shading.
- **Condition**: Condition for which the badge should be obtained. Please mention the official English names of the worlds and effects as to make it easier for the badge to be implemented. If the condition and/or art of the badge is supposed to be secret until obtained, mention it here as well.
- **Internal Triggers (optional)**: Internal condition on which the badge should be triggered (specific map ID, specific switch being ON...). Only mention it if you know it.
- **Art Status**: Whether you are reserving a badge, or you are submitting a finalised badge. Not needed to be mentioned when submitting on Discord as it is obvious per the request done. 
- **Art**: Art of the badge. Your art must be submitted as a 37x37 png file; if you want to submit an animated badge, then a 37x37 gif will need to be added as well (the png will still be used for the chat icon). It is possible to submit a 74x74 png (and gif) under very specific conditions and per request, as mentioned in the [Badge Rules Document], but note that unless the 74x74 size was requested in advance prior to the making, and that said size is required due to zooming effects, entries submitted at that size will automatically be rejected.
- **Art Usage**: Select between "Free to modify", "Requires contact", "Must be used as-is". By default, "Requires contact" is the one used.
- **Notes (optional)**: Notes you have to say on the badge. If you include references as part of the badge name, description or art, please specify it.
- **Badge points**: Quantity of badge points (BPs) the badge should grant. It should be a multiple of 5, and not be 5. If the badge is supposed to be hidden, mention it and write 0.

[Badge Rules Document]: badge_rules_document.md