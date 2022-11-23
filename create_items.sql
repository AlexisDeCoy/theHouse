INSERT INTO items (name, img, description, created_at, updated_at) VALUES ("Trowel", "Trowel.png", "A handheld gardening trowel, made to dig.", NOW(), NOW());
INSERT INTO items (name, img, description, created_at, updated_at) VALUES ("Candles", "Candles.png", "A melted together conglomeration of candles, used but not burnt out.", NOW(), NOW());
INSERT INTO items (name, img, description, created_at, updated_at) VALUES ("Keyring", "KeyRing.png", "A ring of keys, each of which is numbered. There's over 100.", NOW(), NOW());
INSERT INTO items (name, img, description, created_at, updated_at) VALUES ("Lighter", "Lighter.png", "An old fashioned metal cased lighter. It still works.", NOW(), NOW());
INSERT INTO items (name, img, description, created_at, updated_at) VALUES ("Knife", "Knife.png", "A chef's knife from the kitchen. Not sharp, but not dull either.", NOW(), NOW());
INSERT INTO items (name, img, description, created_at, updated_at) VALUES ("Ladle", "Ladle.png", "A wooden ladle. Could have served some superior stew, but not recently.", NOW(), NOW());
INSERT INTO items (name, img, description, created_at, updated_at) VALUES ("Boots", "Boots.png", "A pair of old leather boots, worn and broken in.", NOW(), NOW());
INSERT INTO items (name, img, description, created_at, updated_at) VALUES ("Coat", "Coat.png", "A moth eaten coat covered in dust.", NOW(), NOW());
INSERT INTO items (name, img, description, created_at, updated_at) VALUES ("Scarf", "Scarf.png", "A long scarf, riddled with holes from various insects.", NOW(), NOW());
INSERT INTO items (name, img, description, created_at, updated_at) VALUES ("Mom's Note", "momnote.png", "A short message scrawled on a note pad by your mom. It reads: The nice antique clocks keep stopping at 10:20... -Call repairman", NOW(), NOW());
INSERT INTO items (name, img, description, created_at, updated_at) VALUES ("Day Log", "EbenezerNote.png", "A note found in the hidden room. It reads: Saturday September 17 1887, 10:20PM. THE NEW MOON RISES. I must gather my materials. (Book of Shadows, page. 231)", NOW(), NOW());
INSERT INTO items (name, img, description, created_at, updated_at) VALUES ("The Book Of Shadows", "grimoire.png", "The whole book is written in an illegible scrawl that you can't understand. But on page 231, there are a few written notes around the margins. They read: To perform the ritual... need candles, potion, mirror... sacrifice.", NOW(), NOW());
INSERT INTO items (name, img, description, created_at, updated_at) VALUES ("Note About Gerard", "GerardNote.png", "A note buried with Gerard. It reads: My heart breaks from how much I miss our time together. Every time I go down to the basement, I think back to the day I got you.", NOW(), NOW());
INSERT INTO items (name, img, description, created_at, updated_at) VALUES ("Potion Bottle", "EmptyBottle.png", "A glass bottle, hand blown and not symmetrical", NOW(), NOW());
INSERT INTO items (name, img, description, created_at, updated_at) VALUES ("Potion (Full)", "FullBottle.png", "A glass bottle filled to the brim with fluid.", NOW(), NOW());
INSERT INTO items (name, img, description, created_at, updated_at) VALUES ("Mirror Fragments", "MirrorFragments.png", "Fragments of a broken mirror. There are letters on the back of the pieces. There are three letter Is, an L, and an X.", NOW(), NOW());
INSERT INTO items (name, img, description, created_at, updated_at) VALUES ("Catnip", "Catnip.png", "A stem of catnip", NOW(), NOW());
INSERT INTO items (name, img, description, created_at, updated_at) VALUES ("Milkweed", "Milkweed.png", "A sprig of milkweed.", NOW(), NOW());
INSERT INTO items (name, img, description, created_at, updated_at) VALUES ("Nightshade", "Nightshade.png", "A bouquet of nightshade.", NOW(), NOW());
INSERT INTO items (name, img, description, created_at, updated_at) VALUES ("Wolfsbane", "WolfsBane.png", "A branch of wolfsbane", NOW(), NOW());
INSERT INTO items (name, img, description, created_at, updated_at) VALUES ("Wormwood", "Wormwood.png", "A collection of wormwood leaves.", NOW(), NOW());
INSERT INTO items (name, img, description, created_at, updated_at) VALUES ("Potion Recipe", "Recipe.png", "A recipe for a potion. It reads: Nightshade, Wormwood, Milkweed.", NOW(), NOW());
INSERT INTO items (name, img, description, created_at, updated_at) VALUES ("Mirror (Fixed)", "FixedMirror.png", "A handheld mirror that you've fixed.", NOW(), NOW());

INSERT INTO puzzles (name, created_at, updated_at) VALUES ("Basement Door", NOW(), NOW());
INSERT INTO puzzles (name, created_at, updated_at) VALUES ("Hidden Room", NOW(), NOW());
INSERT INTO puzzles (name, created_at, updated_at) VALUES ("Fixed Mirror", NOW(), NOW());









UPDATE inventory SET item_id = 14 WHERE player_id = 3 and item_id = 15;

select * from players;
select * from items;
select * from puzzles;
select * from solved_puzzles;
select * from inventory WHERE users_id = 1 AND items_id = 2;
select items.id, name, img, description from inventory JOIN items ON items.id = items_id JOIN players ON players.id = users_id WHERE players.id = 5;
delete from players where id=5;
delete from items where id=1;

INSERT INTO inventory (users_id, items_id) VALUES (5, 2);