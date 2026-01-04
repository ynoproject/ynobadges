# Finding Internal Triggers

For a badge to work, an internal trigger needs to be coded, which needs to be searched first.

Outside of Sabitsuki-only badges in .flow and OneShot, when implementing a badge trigger, make sure the badge is coded in such a way that it can be obtained even by players that already completed what needs to be done in the badge, either by doing once more the action or going where the action needs to be done: having to do a new game to get a badge shouldn't be something a player should do.


## Tools Needed

- [RPG Maker 2003](https://store.steampowered.com/app/362870/RPG_Maker_2003/) to find internal triggers by looking inside the games. [RPG Maker 2000](https://store.steampowered.com/app/383730/RPG_Maker_2000/) is not required, as RPG Maker 2003 can also be used to open RPG Maker 2000 games (Yume 2kki, .flow, Mikan Muzou, Ultra Violet, nostAlgic, If), as long as you don't edit the database of the game with it. Alternatively, [R48](https://github.com/20kdc/gabien-app-r48) can also be used, being a free software, but can be harder to install and use. Thus, the instructions here will focus on RPG Maker 2003.
    - If names appear as Mojibake in the editor, you can use [Locale Emulator](https://xupefei.github.io/Locale-Emulator/), and use it on RPG Maker 2003 by selecting a specific language as to be able to see it properly. More info on installing it can be found on [Yume Wiki](https://yume.wiki/2kki/Installation_Instructions#Running_Yume_2kki_without_a_3rd_Party_Software) (steps 1~4 only; applying it for RPG Maker 2003 instead of the RPG_RT, and changing Japanese to whatever language you need).
- [EasyRPG Player](https://easyrpg.org/player/downloads/) to run the games, as it has extremely useful fonctions to playtest and find elements quicker. You can use its Fast Forward function (hold F for x3 speed, G for x10) to do things faster, and the speed can be adjusted in the settings menu (F1) allowing to change the speed set for those keys to go up to x100. Its TestPlay mode can be enabled by either passing the argument `--test-play` to the executable, replacing the executable of the game (RPG_RT.exe) by the EasyRPG Player one and starting the game through RPG Maker, or putting the Player in a folder below the one of your game, and pressing Shift in the game browser while selecting your game to start it in TestPlay mode (this latter option is preferred, as you can put all the games and quickly select between all of them by doing so). While in TestPlay mode, you can press F9 to open the Debug Menu, allowing to check and adjust switches variables, teleport anywhere, give you effects, save anywhere. Also, holding CTRL will allow you to walk through walls, F10 interrupt the current running event, F11 save where you want, and Shift display test instantaneously.
- The [Yume Wiki](https://yume.wiki/) website contains a lot of useful informations to find internal triggers. For instance, by typing the name of the world, you can find the page of a world, with said page listing the map IDs of the world. Some pages also contain a bit of documentation for Yume 2kki, for its [Switches](https://yume.wiki/2kki/Switches), [Variables](https://yume.wiki/2kki/Variables) and [Common Events](https://yume.wiki/2kki/Common_Events): this can be useful if you need to go through them and aren't familiar with Japanese.
- The [ynolocations](https://github.com/ynoproject/ynolocations) repository contains the location configuration for each game on the site (with Yume 2kki being only a partial configuration, the rest of its entries being listed on the [Map IDs](https://yume.wiki/2kki/Map_IDs) wiki page). This can be used to find the map ID of a world, by doing CTRL + F and typing its name, especially if the game is not present on the wiki or if the wiki documentation is not complete.


## Finding a Map ID

To start, you need to know what you are looking for.

Ideally, you already know the name of the world. 

If you don't know the name of the world, but that you know what it looks like, you can either a) dig into the game by checking each map in hope of finding it or b) ask the provider more details as to know the name of the world.

Once you know the name of the world, you can check on Yume Wiki or the ynolocations configuration to which map ID(s) the world is associated. If several map IDs are listed for a world, and that the configuration or Yume Wiki doesn't explicitly tells what it corresponds to, either check the maps in RPG Maker or teleport to them using the Debug Menu of the EasyRPG Player to know which one(s) are those you are looking for.

If the trigger of the badge is just for visiting the world, and that said map ID only contains said world, then you can stop there. Otherwise, we're continuing with the next sections, which will depend on your badge.


## Adding Coordinates

Some badges are intended to be for reaching specific points of a map. It can be of several natures, such as seeing a specific static element, reaching a sub-location of the map, or a world that is present on a multiple-worlds map.

A set of coordinates is comprised of 4 values, the coordinates X and Y of the top-left corner, and the coordinates X and Y of the bottom-right corner of the area you want to define. You can find the coordinates of a tile by clicking on it in RPG Maker, which will display the coordinates next to the map name at the bottom of the screen. Alternatively, some games track the coordinates of the tile you are standing on during gameplay in variables, so you can easily check them while playing by opening the Debug Menu and checking the values of those variables:

- Yume 2kki:
    - Map ID: 26
    - X coordinate: 22
    - Y coordinate: 23
- BRAINGIRL:
    - Map ID: 4
    - X coordinate: 5
    - Y coordinate: 6
- Deep Dreams:
    - Map ID: 104
    - X coordinate: 106
    - Y coordinate: 107
- .flow:
    - Map ID: 7
    - X coordinate: 3
    - Y coordinate: 5
- FOG:
    - X coordinate: 51
    - Y coordinate: 52
- If:
    - Map ID: 5
    - X coordinate: 6
    - Y coordinate: 7
- Mikan Muzou:
    - Map ID: 1
    - X coordinate: 2
    - Y coordinate: 3
- Muma|Rope:
    - X coordinate: 3
    - Y coordinate: 4
- nostAlgic:
    - Map ID: 2
    - X coordinate: 4
    - Y coordinate: 5
- Someday:
    - Map ID: 502
    - X coordinate: 503
    - Y coordinate: 504
- Yume Tsushin:
    - Map ID: 84
    - X coordinate: 85
    - Y coordinate: 86
- Ultra Violet:
    - Map ID: 7
    - X coordinate: 8
    - Y coordinate: 9
- Unaccomplished:
    - X coordinate: 3
    - Y coordinate: 4
- Uneven Dream:
    - Map ID: 5
    - X coordinate: 6
    - Y coordinate: 7

Other games not mentioned do not track it during play, the same goes for the map ID of some of those games.

If a badge is intended for seeing a specific element, define the area to only cover tiles where the element can fully be seen.


## Event

Some badges should trigger upon interacting or colliding with an event. This is rather easy to do: in RPG Maker, select the intended event, press Enter, and check the ID of the event (present in the name of the window).

You now have the ID of the event intended to trigger the badge. You can combine this with the status of a switch, variable, or coordinates, as to only allow the badge to be triggered under specific circumstances (e.g. only while a specific effect is in use).

There are two different ways of setting an event badge: collision with an event, and interaction with an event. An interaction happens when the interaction key (Enter, Z, Space) is pressed which leads to interacting with an event, while a collision is when you or the event enters in collision with each other, leading to its script being triggered. Which property to use can be defined depending on the interaction available in-game, and depending on the Trigger of the event: Action Button is solely for interaction, Event Touch and Player Touch are for collision if the script is triggered upon collision, and both can be used if the event is set at the same priority than the player and that the interaction key can be used.

If an event doesn't do anything when interacted or collided with, note that the badge will not be able to be tracked.


## Previous Map

In some cases, you may want to trigger a badge depending on which map the player was on previously (for instance, upon using a one-way warp).

Doing this type of trigger requires you to know the ID of the new map, and the ID of the previous map, both being able to be found using the Map ID section present above.

In some cases, a game can teleport you across several maps in a row, which may render it a bit unstable. In Yume 2kki case, the game tracks the previous map as part of the variable 99, so its value can be used as an alternative either to circumvent that, or if you don't want Previous Map to be the trigger of the badge.


## Switch/Variable

You may need to check the status of a switch and/or variable depending on the case.

In RPG Maker, switches and variables are solely defined by what the developer decides: their use will depend as such on what the developer decided.

Usually, you will know if you want to use those upon checking the code of the event tied to what you want to track: either its code alters or check the value of a switch or variable, upon which you may need to check its status, or an event may contain several pages, with some only being enabled when a specific switch and/or variable is set: it all depends on how it is coded.


## Picture

Some events display a picture, and checking that the picture of the event is displayed is a possible trigger.

The only argument needed here is the name of the picture: it is specified in RPG Maker when being displayed, but you can also find it in the files of the game. If you pick the name directly from RPG Maker, make sure the filename you are picking isn't Mojibake, otherwise it will not work.

The picture argument may not necessarily the best option, as in some cases the developer may have created a preloading script as part of the map which will create a false positive. Such code is almost never coded, but it can be done in rare cases.


## Misc

Don't forget that several conditions can be put for a single badge, and that alternatives to a trigger can be put: for instance, if you have a badge for visiting a world present on several maps, you can put the different maps as part of the trigger, and make the badge trigger upon visiting one of the maps rather than all of them.


## Map Tree Organisation

Each game organises its map tree in a different way. Depending on the size and organisation, it may be more or less easy to find what you are looking for.

After selecting a map in the maptree, you can type the name of another map to directly open it. This is only possible if the map folder in which the map is located is open, so please keep in mind that.

Solo games sort their map tree based on game design. This is the case with Amillusion, Answered Prayers, `[COLD]`, Deep Dreams, Dream Genie, .flow, FOG, If, Mikan Muzou, nostAlgic, OneShot, Oversomnia, She Awaits, Someday, Yume Tsushin, Ultra Violet, and Yume Nikki.

Muma|Rope mostly groups its maps by order of addition.

Yume 2kki and Uneven Dream, being multiple authors games, group their maps by author.

Some games have the name of their maps match the name of the locations on YNOproject/on the wiki, allowing you to quickly access them by typing their name:
- BRAINGIRL
- FOG (may not be entirely accurate)
- Oversomnia

Some games allow you to quickly access maps just by typing their map ID:
- `[COLD]` (each map have their name starts by the 3 digits of their map ID)
- Deep Dreams (each map have their name starts by the 4 digits of their map ID)
- Dream Genie (*almost* all maps start by MAP followed by the 4 digits of their map ID)
- Unaccomplished (each map have their name starts by the 3 digits of their map ID)
- Uneven Dream (each map have their name starts by the 4 digits of their map ID, in addition to being grouped by author)
- Yume 2kki (each map have their name starts by MAP followed by the 4 digits of their map ID, in addition to being grouped by author)

Lastly, Amillusion, Answered Prayers, FOG, Mikan Muzou (if using English translation), Muma|Rope, OneShot, She Awaits, Someday, and Yume Tsushin use the alphabet for their map names, another method of directly accessing them in RPG Maker is to open EasyRPG Player, open the Debug Menu, check the name of a specific map ID, and type it in RPG Maker. 


### Yume 2kki Map Tree

The Yume 2kki map tree is organised by developers, with each developer having its own map folder assignated. Developers that are proxied are set in a sub-folder of their proxy which can make it hard to find them if this information is not known, and some maps may be in an unusual location/may not be explicit, so here's a basic rundown of map tree info you need to be aware of:
- The map 11 folder contains some of the [Connecting Maps](https://yume.wiki/Category:Yume_2kki_Connecting_Maps), such as Hot Air Balloon World and Sugar Road.
- The map 101 folder contains the maps tied to the default minigame B (maps 101~110).
- The map 121 folder contains the maps tied to the ↑V↑ (Wavy Up) minigame (maps 121~130).
- The map 171 folder contains some of the maps tied to Urotsuki's Dream Apartments (maps 171~180).
- The map 221 folder contains some of the maps tied to the endings as well as the Developer's Room (maps 221~230).
- The map 401 folder contains the maps tied to the GIMMICK RUNNER minigame (maps 401~410).
- The map 501 folder contains the maps tied to the developer Tonden (maps 501~510).
- The map 801 folder contains 2i9's maps, as well as the maps of the developers they are proxying, MymeType and froggo.
- The map 1121 folder contains Yasakoten's maps (やさこてん), as well as the maps of the developers they are proxying, Jared, Mokaccino, ouri, arva, ameato, and eurana.
- The map 1541 folder contains Horatsuki's maps (ほらつき), as well as the maps of the developers they are proxying, Autumn and Cheo.
- The map 1851 folder contains Nakatsu's maps (中津), as well as the maps of the developers they are proxying, Kong, JIVV, Namedude, Colby, openbreeze, Konkyuter, and 001247.
- The map 1861 folder contains FUMO's maps, as well as the maps of the developer they are proxying, Peperoncino III from Yamada Pref. (山田県産ﾍﾟﾍﾟ3世).
- The map 1991 folder contains K0OdntepKs's maps.
- The map 2391 folder contains Nabisae's maps (ナビサエ), as well as the maps of the developers they are proxying, delta_judgment, Fran, lapλace, torifel, and ed2551.
- The map 2461 folder contains oneirokamara's maps (窯良), as well as the maps of the developers they are proxying, Nulsdodage, intelligencecasino, luok, Z4, bean, ZLD1, VinC3R3, nambibaa, madymew, Y24U, and glowwoomii.

Note that this list may be out of date (last updated January 4th, 2026).

Map slots are grouped by 10 (1-10), so for instance, if you see a map with the ID 1543, you already know it is a map slot from Horatsuki.
