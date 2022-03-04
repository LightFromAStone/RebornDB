INSERT INTO out_battle_use (useability_definition)
VALUES
    ('The item cannot be used outside of battle.'),
    ('The item can be used on a Pokémon, and disappears after use (e.g. Potions, Elixirs). The party screen will appear when using this item, allowing you to choose the Pokémon to use it on. Not for TMs and HMs, though.'),
    ('The item can be used out of battle, but it isn''t used on a Pokémon (e.g. Repel, Escape Rope, usable Key Items.)'),
    ('The item is a TM. It teaches a move to a Pokémon, but does not disappear after use.'),
    ('The item is a HM. It teaches a move to a Pokémon, but does not disappear after use. Moves taught by a HM cannot be forgotten.'),
    ('The item can be used on a Pokémon, but it does not disappear after use (e.g. Poké Flute).'),
    ('The item is a TR. It teaches a move to a Pokémon, and disappears after use.');

INSERT INTO in_battle_use (useability_definition)
VALUES
    ('The item cannot be used in battle.'),
    ('The item can be used on one of your party Pokémon, and disappears after use (e.g. Potions, Elixirs). The party screen will appear when using this item, allowing you to choose the Pokémon to use it on.'),
    ('The item can be used on one of the moves known by one of your party Pokémon, and disappears after use (e.g. Ether). The party screen will appear when using this item, followed by a list of moves to choose from.'),
    ('The item is used on the Pokémon in battle that you are choosing a command for (e.g. X Accuracy). It disappears after use.'),
    ('The item is used on an opposing Pokémon in battle, and disappears after use (Poké Balls). If there is more than one opposing Pokémon, you will be able to choose which of them to use it on.'),
    ('The item is used with no target, and disappears after use (e.g. Poké Doll, Guard Spec.).'),
    ('The item can be used on one of your party Pokémon, and the item is not consumed after use (Blue Flute). The party screen will appear when using this item, allowing you to choose the Pokémon to use it on.'),
    ('The item can be used on one of the moves known by one of your party Pokémon, and is not consumed after use. The party screen will appear when using this item, followed by a list of moves to choose from.'),
    ('The item is used on the Pokémon in battle that you are choosing a command for. It remains after use.(Red/Yellow Flutes).'),
    ('The item is used on an opposing Pokémon in battle, and remains after use. If there is more than one opposing Pokémon, you will be able to choose which of them to use it on.'),
    ('The item is used with no target, and remains after use (Poké Flute).');

INSERT INTO special_items_use (useability_definition)
VALUES
    ('The item has no special use.'),
    ('The item is a Mail item.'),
    ('The item is a Mail item, and the images of the holder and two other party Pokémon appear on the Mail.'),
    ('The item is a Snag Ball (i.e. it can capture enemy trainers'' Shadow Pokémon).'),
    ('The item is a Poké Ball item.'),
    ('The item is a berry that can be planted.'),
    ('The item is a Key Item.'),
    ('The item is an evolution stone.'),
    ('The item is a fossil that can be revived.'),
    ('The item is an Apricorn that can be converted into a Poké Ball.'),
    ('The item is an elemental power-raising Gem.'),
    ('The item is mulch that can be spread on berry patches.'),
    ('The item is a Mega Stone. This does NOT include the Red/Blue Orbs.');