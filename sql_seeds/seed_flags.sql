INSERT INTO flags (flag_value, flag_description)
VALUES
('a', 'The move makes physical contact with the target'),
('b', 'The target can use Protect or Detect to protect itself from the move'),
('c', 'The target can use Magic Coat to redirect the effect of the move. Use this flag if the move deals no damage but causes a negative effect on the target. (Flags c and d are mutually exclusive.)'),
('d', 'The target can use Snatch to steal the effect of the move. Use this flag for most moves that target the user. (Flags c and d are mutually exclusive.)'),
('e', 'The move can be copied by Mirror Move'),
('f', 'The move has a 10% chance of making the opponent flinch if the user is holding a King''s Rock/Razor Fang. Use this flag for all damaging moves that don''t already have a flinching effect'),
('g', 'If the user is frozen, the move will thaw it out before it is used'),
('h', 'The move has a high critical hit rate'),
('i', 'The move is a biting move (powered up by the ability Strong Jaw)'),
('j', 'The move is a punching move (powered up by the ability Iron Fist)'),
('k', 'The move is a sound-based move'),
('l', 'The move is a powder-based move (Grass-type Pokémon are immune to them)'),
('m', 'The move is a pulse-based move (powered up by the ability Mega Launcher)'),
('n', 'The move is a bomb-based move (resisted by the ability Bulletproof)'),
('o', 'The move is a dance move (repeated by the ability Dancer)');