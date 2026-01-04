# Handling the Badge Sheet

The Badge Sheet is made out of several pages.

Here are the three main pages that will be frequently checked and used:

* Reservations: List of badges that are currently reserved.
* Waiting_Sheet: List of badges that are waiting for implementation, or in the process of being implemented.
* Form_Submissions: This is where entries submitted through the [Google Forms](https://forms.gle/tWJNdG8pTS1vNtGb8) by artists are listed.

Details on the other pages are provided on the index of the badge sheet, but are not always required.


# What Needs to Be Done

On the `#badge-proposal` channel of the Discord server, entries will be submitted by artists. Depending on the case, what needs to be done will depend:

- Is it an update to an existing entry on the Reservations page by said artist?
    - If so, after checking the entry (see next section), fill the entry on the Reservations page, and if the entry is complete and valid, move it to the Waiting_Sheet.
- Is it an update to an existing badge by the same artist that is already implemented, a replacement of an existing badge, or a replacement of a badge that was removed?
    - If so, after checking the entry, note it down (either for yourself or on the sheet), and remember to update it the next time you work on badges.
- Is the badge a reservation of a new entry?
    - If so, after checking the entry and making sure it is valid, add it to the Reservations page.
- Is the badge a finished entry that was not already present on the sheet?
    - If so, after checking the entry and making sure it is valid, add it to the Waiting_Sheet page.

If the entry is considered invalid, explain it to the user. Depending on the case, it may simply require a tweak (change of name, resending the art, adjusting the art...) or the entry may have to be entirely declined (conflicting badge).

Some artists will submit their badges using the form. In this case, the entry will already be present on the Form_Submissions page.
- If the entry is a complete entry and is valid, move it to the Waiting_Sheet page.
- If the entry is a reservation and is valid, move it to the Reservations page.
- If the entry is not considered valid, add a comment explaining the reasoning why in Dev Comments or Further Comments, and adjust the Chance of Implement accordingly. After a few days, as to let time for the artist to see the comment, move the entry to the Badge_Mausoleum.

When using the [Badge Tools](badge_tools.md) to generate badges, the entries that are added are those present in the Waiting_Sheet, as those are complete entries.

Once the badges are implemented (merged into the ynobadges repository), change the Chance of Implement of those badges to `✔`, and move them to the Badge_Mausoleum.

To move an entry or several entries between pages, select the row of the entry, copy it, and paste it on the new page. On the old page, delete the row of the entry once done.

If an entry present on the Reservations page reached its deadline, said entry should be moved to the Badge_Mausoleum, specifying its deadline was reached, and mentioning it in the `#badge-proposal` channel should be done as to let interested users the possibility to reserve it.


## Checking an Entry

- Make sure the date of reservation of the entry is present.
- For the badge name, description and condition, unless it makes sense, those text fields should use American English, and consistency on punctuation should be put: if one of those characters is used, rather than using `…`, `—`, `？`, `’`, `“`, `”`, please use `...`, `-`, `?`, `'`, `"`, `"`. Do not use emojis as part of the text fields, as the shading of the UI may look off on them.
- Make sure the name of the badge is unique, not too close to an existing badge, is in [Title Case](https://en.wikipedia.org/wiki/Title_case), is appropriate and makes sense.
- Make sure the Target Game is correct.
- Make sure the name of the artist is correct, is not too close to the name of another existing artist to avoid confusion, and is identical to how it is written in other entries and existing badges. If there are several artists, separate them with `,` and `&` characters (e.g. `Allan, Benjamin, Chloé & Daniel`, `Estelle & Folia`). For simplicity, ideally, artists should have their name be only made of characters from the ASCII table.
- If the entry submitted does not fill the description field, or the artist writes something like --- for it, make the description field be empty. While content in said field can be a bit free on how it is written, proofreading, consistency, being appropriate and it making sense is nonetheless required.
- Write the condition text in a similar way than existing entries, formal and clear to the user. If the condition text is made out of several sentences, each sentence should end with a dot. If it is made of only one sentence, no need for any dot. Make sure the proper vocabulary for the condition is used (proper name of the effects, collectibles, worlds), and for consistency, basing the condition text on the formatting used by existing similar badges can be done. Make sure the condition does not conflict with an existing badge or existing entry (check on each page of the badge sheet using CTRL + F, in addition to checking the [badge list](https://github.com/ynoproject/ynobadges/blob/master/lang/en.json)), and is not too close to an existing badge or entry.
- Add an internal trigger to the badge: while it is not necessary for it to be added right away, make sure you check and/or know that the badge **is** trackable before accepting it. Writing internal triggers in a similar way to existing triggers can be done if wanted, as to have things clear for anyone picking up the sheet.
- Make sure the BPs are a multiple of 5 but not 5, are 0 if the badge is planned to be hidden, and that the BPs overall match the difficulty of the badge: don't hesitate to adjust them if you think the badge should grant more or less BPs.
- Make sure the art is in the 37x37 resolution, unless specifically authorised after discussion with the badge committee/moderation team to be in the 74x74 resolution. Make sure the art is not heavily compressed (if the art submitted ends up being a 36x36 png, it is heavily compressed and needs to be resent). If the badge is intended to be animated, make sure both a gif and a png files are present. Make sure the art is of quality, accurately represents the content depicted, doesn't plagiarize anything and doesn't rip assets from the game for it.
- Make sure the Art Status is properly set to Done if the badge is complete, and to Reserved otherwise.
- Make sure an Art Usage is set. if none was specified, set it to Requires contact.
- Make sure the Reservation Deadline was added to the entry if it is a reservation, and that no Reservation Deadline is present if it is a complete entry. No need to type the Reservation Deadline manually unless its deadline was extended, as copying it from another field that has it set up will automatically make it be for 3 months after the reservation date.

If you are unsure about any of those points, and specifically for the badge name, description, art, or redundancy, feel free to discuss it with the moderation team or badge committee.

Check the [Badge Submission](badge_submission.md) and [Badge Rules Document](badge_rules_document.md) also, as some additional points, rules, and different wordings may be present.


## Troubleshooting

- If the software used by an artist forces 37x37 png files to be sent at a 36x36 resolution, all compressed, you can check with the artist if sending the static art as a gif sends it at the 37x37 resolution. If the gif doesn't end up being compressed, you can convert it to the png format and use it for the badge.
- Artists using the form to submit entries may not necessarily be easily contactable. Don't hesitate to ask to moderators, to the badge committee or in `#badge-proposal` if anyone knows where/how they can be contacted.
- CTRL + F is your best friend, whether it is too quickly check entries on a page, checking existing badges, or checking if an artist is indeed who they claim to be.


## Others

When a new game is added, the Google Forms must be edited to add the new game as part of the entries, while the game column of the main sheets should have their data validation edited to add the new game.