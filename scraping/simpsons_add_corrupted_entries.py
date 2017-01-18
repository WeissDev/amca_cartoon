#!/usr/bin/python
# This file is used to manually add the corrupted entries of the simpsons_script_lines.csv to the database
from __future__ import print_function
import MySQLdb
import csv

db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                     user="pma",  # your username
                     passwd="admin",  # your password
                     db="acma_cartoon")  # name of the data base

cur = db.cursor()

data = []

data.append(
    ['8152', '28', '13', 'Gulliver Dark: (SINGING) "THE RULES THAT CONSTRAIN OTHER MEN / MEAN NOTHING TO MCBAIN...',
     '115000', 'true', '187', '332', 'Gulliver Dark', 'Aztec Theater',
     'THE RULES THAT CONSTRAIN OTHER MEN / MEAN NOTHING TO MCBAIN...',
     'the rules that constrain other men mean nothing to mcbain', '10'])
data.append(
    ['8153', '28', '14', 'Jasper Beardly: Booo.', '123000', 'true', '273', '332', 'Jasper Beardly', 'Aztec Theater',
     'Booo.', 'booo', '1'])
data.append(
    ['8154', '28', '15', 'Gulliver Dark: THE PUNCHES THAT BRING PAIN TO OTHER MEN', '125000', 'true', '187', '332',
     'Gulliver Dark', 'Aztec Theater', 'THE PUNCHES THAT BRING PAIN TO OTHER MEN',
     'the punches that bring pain to other men', '8'])
data.append(
    ['5432', '19', '5', 'Bart Simpson: (WRITING) "One o\'clock -- still just a potato.', '104000', 'true', '8', '5',
     'Bart Simpson', 'Simpson Home', 'One o\'clock -- still just a potato.', 'one oclock -- still just a potato', '7'])
data.append(['5433', '19', '6',
             'Ned Flanders: (PLEASANTLY) "Hey there, neighbor! The Lord\'s certainly given us a beautiful day today. Huh?"',
             '108000', 'true', '11', '5', 'Ned Flanders', 'Simpson Home',
             'Hey there, neighbor! The Lord\'s certainly given us a beautiful day today. Huh?',
             'hey there neighbor the lords certainly given us a beautiful day today huh', '13'])
data.append(['5358', '18', '212', 'Tony Bennett: "IT\'S AGAINST THE LAW TO FROWN /', '1028000', 'true', '297', '239',
             'Tony Bennett', 'Capital City',
             'IT\'S AGAINST THE LAW TO FROWN /', 'its against the law to frown', '6'])
data.append(['5443', '19', '16', 'Marge Simpson: "Oh, well, we\'re all out Homer."', '144000', 'true', '1', '5',
             'Marge Simpson', 'Simpson Home',
             "Oh, well, we're all out, Homer.", 'oh well were all out homer', '6'])
data.append(['5354', '18', '208', 'Tony Bennett: "AND IT MAKES A KING FEEL LIKE/', '1016000', 'true', '297', '239',
             'Tony Bennett', 'Capital City', 'AND IT MAKES A KING FEEL LIKE', 'and it makes a king feel like', '7']
            )
data.append(['5355', '18', '209', 'Tony Bennett: SOME NUTTY KOO-KOO SUPER-KING...', '1019000', 'true', '297', '239',
             'Tony Bennett', 'Capital City', 'SOME NUTTY KOO-KOO SUPER-KING...', 'some nutty koo-koo super-king', '4'])
data.append(['5351', '18', '205', 'Tony Bennett: "IT\'S THE KIND OF PLACE THAT MAKES', '1009000', 'true', '297', '239',
             'Tony Bennett', 'Capital City', 'IT\'S THE KIND OF PLACE THAT MAKES', 'its the kind of place that makes',
             '7']
            )
data.append(
    ['5352', '18', '206', 'Tony Bennett: A BUM / FEEL LIKE A KING...', '1009000', 'true', '297', '239', 'Tony Bennett',
     'Capital City', 'A BUM / FEEL LIKE A KING...', 'a bum feel like a king', '6'])
data.append(['5348', '18', '202', 'Tony Bennett: "PEOPLE STOP AND SCREAM HELLO"', '1001000', 'true', '297', '239',
             'Tony Bennett', 'Capital City',
             'PEOPLE STOP AND SCREAM HELLO', 'people stop and scream hello', '5']
            )
data.append(['5349', '18', '203', 'Tony Bennett: IN CAPITAL CITY...',
             '1004000', 'true', '297', '239', 'Tony Bennett', 'Capital City', 'IN CAPITAL CITY..."', 'in capital city',
             '3'])
data.append(['5345', '18', '199', 'Tony Bennett: "THERE\'S A SWINGIN\' TOWN I KNOW', '993000', 'true', '297', '239',
             'Tony Bennett', 'Capital City', 'THERE\'S A SWINGIN\' TOWN I KNOW', 'theres a swingin town i know', '6']
            )
data.append(['5346', '18', '200', 'Tony Bennett: CALLED CAPITAL CITY...',
             '997000', 'true', '297', '239', 'Tony Bennett', 'Capital City', 'CALLED CAPITAL CITY...',
             'called capital city', '3'])
data.append(
    ['4263', '14', '255', 'Entire Town: "GONE AWAY IS THE BLUEBIRD / HERE TO STAY...', '1141000', 'true', '241', '211',
     'Entire Town', 'NEIGHBORHOOD',
     'GONE AWAY IS THE BLUEBIRD / HERE TO STAY...', 'gone away is the bluebird here to stay', '8']
)
data.append(['4264', '14', '256', 'Bart Simpson: Gotta study! Gotta study! Gotta study!', '1149000', 'true', '8', '211',
             'Bart Simpson', 'NEIGHBORHOOD', 'Gotta study! Gotta study! Gotta study!',
             'gotta study gotta study gotta study', '6'])
data.append(['4265', '14', '257', '(Simpson Home: int. simpson house - basement)', '1154000', 'false', '', '5', '',
             'Simpson Home', '', '', ''])
data.append(['4266', '14', '258',
             'Bart Simpson: (READING ALOUD WITH HEART) "Chapter Six: Four Days in Philadelphia. The first Continental Congress faced a difficult job. Could the delegates agree on recommendations that all Americans could support?"',
             '1154000', 'true', '8', '5', 'Bart Simpson', 'Simpson Home',
             'Chapter Six: Four Days in Philadelphia. The first Continental Congress faced a difficult job. Could the delegates agree on recommendations that all Americans could support?',
             'chapter six four days in philadelphia the first continental congress faced a difficult job could the delegates agree on recommendations that all americans could support',
             '25'])
data.append(['4267', '14', '259', '(CONTINENTAL CONGRESS PHILADELPHIA: int. continental congress, philadelphia - 1776)',
             '1160000', 'false', 'NULL', '212', 'NULL',
             'CONTINENTAL CONGRESS, PHILADELPHIA', 'NULL', 'NULL', 'NULL'])
data.append(['4260', '14', '252', 'Entire Town: "SLEIGH BELLS RING ARE YOU LISTENIN\'', '1121000', 'true', '241', '211',
             'Entire Town', 'NEIGHBORHOOD',
             'SLEIGH BELLS RING / ARE YOU LISTENIN\'', 'sleigh bells ring are you listenin', '6']
            )
data.append(['4261', '14', '253', 'Entire Town: IN THE LANE / SNOW IS GLISTENIN\'', '1130000', 'true', '241', '211',
             'Entire Town', 'NEIGHBORHOOD', 'IN THE LANE / SNOW IS GLISTENIN', 'in the lane snow is glistenin', '6'])
data.append(
    ['4262', '14', '254', 'Entire Town: A BEAUTIFUL SIGHT / WE\'RE HAPPY TONIGHT/ WALKIN\' IN A WINTER WONDERLAND.',
     '1134000', 'true', '241', '211', 'Entire Town', 'NEIGHBORHOOD',
     'A BEAUTIFUL SIGHT / WE\'RE HAPPY TONIGHT/ WALKIN\' IN A WINTER WONDERLAND.',
     'a beautiful sight were happy tonight walkin in a winter wonderland', '11'])
data.append(
    ['4268', '14', '260', 'Thomas Jefferson: "We hold these truths to be self-evident."', '1160000', 'true', '242',
     '212', 'Thomas Jefferson', 'CONTINENTAL CONGRESS, PHILADELPHIA', 'We hold these truths to be self-evident.',
     'we hold these truths to be self-evident', '7']
)
data.append(
    ['4357', '15', '49', '(WINFIELD\'S HOUSE: EXT. WINFIELD\'S HOUSE - CONTINUOUS)', '317000', 'false', '', '215', '',
     'WINFIELD\'S HOUSE', '', '', ''])
data.append(['4213', '14', '205',
             'Martin Prince: Who would have thought that pushing a boy into the girls\' lavatory could be such a thrill? The screams, the humiliation, the fact that it wasn\'t me. I\'ve never felt so alive.',
             '895000', 'true', '38', '3', 'Martin Prince',
             'Springfield Elementary School',
             'Who would have thought that pushing a boy into the girls\' lavatory could be such a thrill? The screams, the humiliation, the fact that it wasn\'t me. I\'ve never felt so alive.',
             'who would have thought that pushing a boy into the girls lavatory could be such a thrill the screams the humiliation the fact that it wasnt me ive never felt so alive',
             '32'])
data.append(
    ['152461', '546', '20', 'ABRAHAM LINCOLN: (FURIOUS) Guess what. I also play Frankenstein! (FRANKENSTEIN GROWL)',
     '105000', 'true', '857', '3', 'ABRAHAM LINCOLN', 'Springfield Elementary School',
     'Guess what. I also play Frankenstein!', 'guess what i also play frankenstein', '6']
)
data.append(['140906', '503', '142',
             'Homer Simpson: (CAUTIOUS) "Override self-destruct protocol with authorization code (PUNCHING IT IN) seven-two-two-five."',
             '649000', 'true', '2', '10', 'Homer Simpson', 'Springfield Nuclear Power Plant',
             'Override self-destruct protocol with authorization code seven-two-two-five.',
             'override self-destruct protocol with authorization code seven-two-two-five', '7']
            )
data.append(
    ['140907', '503', '143', 'Robot: (CALM MALE VOICE) Human interaction mode activated. Initiate conversation.',
     '649000', 'true', '624', '10', 'Robot',
     'Springfield Nuclear Power Plant', 'Human interaction mode activated. Initiate conversation.',
     'human interaction mode activated initiate conversation', '6'])
data.append(['140908', '503', '144', 'Homer Simpson: (TENTATIVE) Will you be my friend?', '662000', 'true', '2', '10',
             'Homer Simpson', 'Springfield Nuclear Power Plant', 'Will you be my friend?', 'will you be my friend',
             '5'])
data.append(['140909', '503', '145',
             'Robot: Friendship cannot exist between man and machine. But I can simulate interest in your statements.',
             '664000', 'true',
             '624', '10', 'Robot', 'Springfield Nuclear Power Plant',
             'Friendship cannot exist between man and machine. But I can simulate interest in your statements.',
             'friendship cannot exist between man and machine but i can simulate interest in your statements', '15'])
data.append(['140910', '503', '146',
             'Homer Simpson: (DELIGHTED GASP) You\'re not a friend... you\'re my best friend. (HUGS IT, THEN:) Uh just don\'t ask me to drive you to the airport.',
             '669000', 'true', '2', '10',
             'Homer Simpson', 'Springfield Nuclear Power Plant',
             'You\'re not a friend... you\'re my best friend. Uh, just don\'t ask me to drive you to the airport.',
             'youre not a friend youre my best friend uh just dont ask me to drive you to the airport', '19'])
data.append(
    ['127763', '454', '146', 'Marge Simpson: (READING) The patrollers were too fast for Eliza and Virgil...', '623000',
     'true', '1', '248', 'Marge Simpson', 'Library', 'The patrollers were too fast for Eliza and Virgil...',
     'the patrollers were too fast for eliza and virgil', '9']
)
data.append(
    ['127764', '454', '147', 'Marge Simpson: Luckily they chanced upon a traveling circus...', '632000', 'true', '1',
     '248', 'Marge Simpson', 'Library', 'Luckily they chanced upon a traveling circus...',
     'luckily they chanced upon a traveling circus', '7'])
data.append(
    ['127765', '454', '148', '(Traveling Circus: ext. traveling circus - field - night (1860))', '639000', 'false', '',
     '3699', '', 'Traveling Circus', '', '', ''])
data.append(
    ['127766', '454', '149', 'Marge Simpson: ...where they were helped by a crusty old clown.', '639000', 'true', '1',
     '3699', 'Marge Simpson', 'Traveling Circus', '...where they were helped by a crusty old clown.',
     'where they were helped by a crusty old clown', '9'])
data.append(['127767', '454', '150',
             'Circus Clown: A little schmutz, a little schmear, and presto -- you\'re part of the under-clown railroad! So you got any talent?',
             '643000', 'true', '5561', '3699', 'Circus Clown', 'Traveling Circus',
             'A little schmutz, a little schmear, and presto -- you\'re part of the under-clown railroad! So you got any talent?',
             'a little schmutz a little schmear and presto -- youre part of the under-clown railroad so you got any talent',
             '20'])
data.append(['125627', '445', '216', 'Moe Szyslak: "The reason I left you is simple:', '1095000', 'true', '17', '15',
             'Moe Szyslak', "Moe's Tavern",
             'The reason I left you is simple:', 'the reason i left you is simple', '7']
            )
data.append(['125628', '445', '217', 'Marge Simpson: (SHOCKED) ...I\'m gay?!',
             '1095000', 'true', '1', '15', 'Marge Simpson', "Moe's Tavern", "...I'm gay?!", 'im gay', '2'])
data.append(['111237', '390', '16', 'Lisa Simpson: ...Hitachee Tribe. (NERVOUS GIGGLE)', '117000', 'true', '9', '6',
             'Lisa Simpson', 'KITCHEN', '...Hitachee Tribe.', 'hitachee tribe', '2']
            )
data.append(['111238', '390', '17',
             'Lisa Simpson: Wait, is it wrong for me to appropriate the culture of a long-suffering people?', '117000',
             'true', '9', '6',
             'Lisa Simpson', 'KITCHEN',
             'Wait, is it wrong for me to appropriate the culture of a long-suffering people?',
             'wait is it wrong for me to appropriate the culture of a long-suffering people', '14'])
data.append(
    ['96708', '335', '274', 'Patty Bouvier: "Are you a \'Patty\' or a \'Selma?\' Take our quiz.', '1223000', 'true',
     '10', '53', 'Patty Bouvier', 'Burns Manor',
     "Are you a 'Patty' or a 'Selma?' Take our quiz.", 'are you a patty or a selma take our quiz', '10']
)
data.append(
    ['96709', '335', '275', 'Captain Horatio McCallister: Well, blow me down, I\'m a Selma.', '1227000', 'true', '944',
     '53', 'Captain Horatio McCallister', 'Burns Manor',
     "Well, blow me down, I'm a Selma.", 'well blow me down im a selma', '7'])
data.append(
    ['91095', '315', '284', 'Homer Simpson: "I-M-O--', '1220000', 'true', '2', '5', 'Homer Simpson', 'Simpson Home',
     'I-M-O--', 'i-m-o--', '1']
)
data.append(['91096', '315', '285', 'Homer Simpson: --K. Get it? "I am OK."', '1220000', 'true', '2', '5',
             'Homer Simpson', 'Simpson Home', '--K. Get it? "I am OK."', '--k get it i am ok', '6'])
data.append(['88907', '308', '85',
             'Homer Simpson: (READING) "Nausea... cravings... knocked-up feeling..." (REALIZING) She was pregnant with Bart! And that\'s the reason she stayed with me.',
             '393000', 'true', '2', '15', 'Homer Simpson', "Moe's Tavern",
             "Nausea... cravings... knocked-up feeling... She was pregnant with Bart! And that's the reason she stayed with me.",
             'nausea cravings knocked-up feeling she was pregnant with bart and thats the reason she stayed with me',
             '17']
            )
data.append(['88908', '308', '86', 'Marge Simpson: I found the missing puzzle piece. It was under Maggie\'s eyelid!',
             '401000', 'true', '1', '15', 'Marge Simpson', "Moe's Tavern",
             'I found the missing puzzle piece. It was under Maggie\'s eyelid!',
             'i found the missing puzzle piece it was under maggies eyelid', '11'])
data.append(
    ['88909', '308', '87', 'Homer Simpson: (FLAT) How \'bout that?', '406000', 'true', '2', '15', 'Homer Simpson',
     "Moe's Tavern",
     'How \'bout that?', 'how bout that', '3'])
data.append(['88910', '308', '88', 'Marge Simpson: It\'s James Taylor', '407000', 'true', '1', '15', 'Marge Simpson',
             "Moe's Tavern",
             'It\'s James Taylor!', 'its james taylor', '3'])
data.append(
    ['88911', '308', '89', 'Homer Simpson: (FLATLY) Oh, the popular singer slash songwriter slash puzzle piece.',
     '409000', 'true', '2', '15', 'Homer Simpson',
     "Moe's Tavern", 'Oh, the popular singer slash songwriter slash puzzle piece.',
     'oh the popular singer slash songwriter slash puzzle piece', '9'])
data.append(
    ['87170', '302', '13', 'Lisa Simpson: (READING) "Molochai desiratum maledictu... nosferatu ascendum corporalis...',
     '147000', 'true', '9', '5', 'Lisa Simpson', 'Simpson Home',
     'Molochai desiratum maledictu... nosferatu ascendum corporalis...',
     'molochai desiratum maledictu nosferatu ascendum corporalis', '6']
)
data.append(['87171', '302', '14', 'Lisa Simpson: (READING) Diabolicus abominabolis...', '147000', 'true', '9', '5',
             'Lisa Simpson', 'Simpson Home', 'Diabolicus abominabolis...', 'diabolicus abominabolis', '2'])
data.append(
    ['87172', '302', '15', 'Lisa Simpson: Ooh, Mad libs!', '147000', 'true', '9', '5', 'Lisa Simpson', 'Simpson Home',
     'Ooh, Mad libs!', 'ooh mad libs', '3'])
data.append(['83465', '289', '164', 'Robert Pinsky: "Impossible to tell in writing.', '670000', 'true', '3592', '2425',
             'Robert Pinsky', 'Caf Kafka', 'Impossible to tell in writing.', 'impossible to tell in writing ', '6']
            )
data.append(
    ['83466', '289', '165', 'Robert Pinsky: He named himself, \'Banana Tree\'...', '672000', 'true', '3592', '2425',
     'Robert Pinsky', 'Caf Kafka', 'He named himself, \'Banana Tree\'...', 'he named himself banana tree',
     '5'])
data.append(['81724', '282', '279',
             'Revue Cast Members: "WE\'RE THE PERFORMERS YOU THOUGHT WERE DEAD / LIKE BONNIE FRANKLIN...AND ADRIAN ZMED...',
             '1068000', 'true', '3510', '2370', 'Revue Cast Members', 'Branson Theater',
             "WE'RE THE PERFORMERS YOU THOUGHT WERE DEAD / LIKE BONNIE FRANKLIN...AND ADRIAN ZMED...",
             'were the performers you thought were dead like bonnie franklinand adrian zmed',
             '12']
            )
data.append(
    ['81725', '282', '280', '(Stage: Ext. stage - wide shot)', '1075000', 'false', '', '856', '', 'Stage', '', '', ''])
data.append(['81726', '282', '281',
             'Revue Cast Members: / BRANSON\'S THE PLACE / WE CAN ALWAYS BE FOUND / THEY TOOK NICK AT NIGHT / AND MADE IT A TOWN.',
             '1075000', 'true', '3510', '856', 'Revue Cast Members', 'Stage',
             '/ BRANSON\'S THE PLACE / WE CAN ALWAYS BE FOUND / THEY TOOK NICK AT NIGHT / AND MADE IT A TOWN.',
             'bransons the place we can always be found they took nick at night and made it a town', '18'])
data.append(
    ['69807', '243', '292', 'Marge Simpson: (CONTINUING) My gold is in the heart of every freedom-loving American.',
     '1145000', 'true', '1', '422', 'Marge Simpson', 'White House',
     'My gold is in the heart of every freedom-loving American.',
     'my gold is in the heart of every freedom-loving american', '10']
)
data.append(['69808', '243', '293', 'Homer Simpson: Ah crap!', '1145000', 'true', '2', '422', 'Homer Simpson',
             'White House', 'Ah, crap!', 'ah crap', '2'])
data.append(['62483', '220', '100',
             'ABBA: "If you wanna be my lover / You gotta get with my friends / Makin\' love forever / Friendship\'s where that ends / If you wanna be my lover...',
             '551000', 'true', '2739', '1902', 'ABBA', "Red's Truck",
             "If you wanna be my lover / You gotta get with my friends / Makin' love forever / Friendship's where that ends / If you wanna be my lover...",
             'if you wanna be my lover you gotta get with my friends makin love forever friendships where that ends if you wanna be my lover',
             '25']
            )
data.append(['62484', '220', '101', 'Homer Simpson: (DREAMILY) Yeah... the open road.', '559000', 'true', '2', '1902',
             'Homer Simpson', "Red's Truck",
             'Yeah... the open road.', 'yeah the open road', '4'])
data.append(
    ['62485', '220', '102', 'Homer Simpson: (BITTER) That little punk. I\'ll teach him some manners.', '565000', 'true',
     '2', '1902', 'Homer Simpson', "Red's Truck", 'That little punk. I\'ll teach him some manners.',
     'that little punk ill teach him some manners', '8'])
data.append(
    ['62486', '220', '103', 'Bart Simpson: No, Dad. He wants you to blow your horn.', '571000', 'true', '8', '1902',
     'Bart Simpson', "Red's Truck",
     'No, Dad. He wants you to blow your horn.', 'no dad he wants you to blow your horn', '9'])
data.append(['17667', '59', '87', 'Singers: (SINGING) "IT\'S THE FIRST ANNUAL MONTGOMERY BURNS / AWARD FOR --',
             '442000', 'true', '276', '636', 'Singers',
             'Springfield Civic Center', "IT'S THE FIRST ANNUAL MONTGOMERY BURNS/ AWARD FOR --",
             'its the first annual montgomery burns award for --', '9']
            )
data.append(['17668', '59', '88', 'Men Singers: (SINGING) OUTSTANDING ACHIEVEMENT IN -', '450000', 'true', '826', '636',
             'Men Singers', 'Springfield Civic Center', 'OUTSTANDING ACHIEVEMENT IN -', 'outstanding achievement in -',
             '4'])
data.append(
    ['17669', '59', '89', 'Female Singers: (SINGING) THE FIELD OF --', '454000', 'true', '827', '636', 'Female Singers',
     'Springfield Civic Center',
     'THE FIELD OF --', 'the field of --', '4'])
data.append(['17670', '59', '90', 'Singers: (SINGING) EXCELLENCE!', '455000', 'true', '276', '636', 'Singers',
             'Springfield Civic Center', 'EXCELLENCE!"', 'excellence', '1'])


query = ''
with open('./simpsons_original_files/simpsons_script_lines.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    columns = next(reader)
    query = 'insert into simpsons_script_lines({0}) values ({1})'
    query = query.format(','.join(columns), ','.join(['%s' for i in range(len(columns))]))


for line in data:
    for i in range(len(line)):
        if line[i] == '':
            line[i] = 'NULL'
    if len(line) == 13:
        cur.execute(query, line)
    else:
        print(line)

db.commit()

db.close()
