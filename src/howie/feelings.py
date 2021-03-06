"""
Guesses feelings and needs as described by nonviolent communication using huggingface pipelines

    Copyright (C) 2022  Sioan Zohar

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

nuanced_feelings = {"AFFECTIONATE":[
"compassionate",
"friendly",
"loving",
"open hearted",
"sympathetic",
"tender",
"warm"],
"ENGAGED":[
"absorbed",
"alert",
"curious",
"engrossed",
"enchanted",
"entranced",
"fascinated",
"interested",
"intrigued",
"involved",
"spellbound",
"stimulated"],
"HOPEFUL":[
"expectant",
"encouraged",
"optimistic"],
"CONFIDENT":[
"empowered",
"open",
"proud",
"safe",
"secure"],
"EXCITED":[
"amazed",
"animated",
"ardent",
"aroused",
"astonished",
"dazzled",
"eager",
"energetic",
"enthusiastic",
"giddy",
"invigorated",
"lively",
"passionate",
"surprised",
"vibrant"],
"GRATEFUL":[
"appreciative",
"moved",
"thankful",
"touched"],
"INSPIRED":[
"amazed",
"awed",
"wonder",
"JOYFUL",
"amused",
"delighted",
"glad",
"happy",
"jubilant",
"pleased",
"tickled"],
"EXHILARATED":[
"blissful",
"ecstatic",
"elated",
"enthralled",
"exuberant",
"radiant",
"rapturous",
"thrilled"],
"PEACEFUL":[
"calm",
"clear headed",
"comfortable",
"centered",
"content",
"equanimous",
"fulfilled",
"mellow",
"quiet",
"relaxed",
"relieved",
"satisfied",
"serene",
"still",
"tranquil",
"trusting"],
"REFRESHED":[
"enlivened",
"rejuvenated",
"renewed",
"rested",
"restored",
"revived"],
"PEACEFUL":[
"tranquil",
"calm",
"content",
"engrossed",
"absorbed",
"expansive",
"serene",
"loving",
"blissful",
"satisfied",
"relaxed",
"relieved",
"quiet",
"carefree",
"composed",
"fulfilled"],
"LOVING":[
"warm",
"affectionate",
"tender",
"appreciative",
"friendly",
"sensitive",
"compassionate",
"grateful",
"nurtured",
"amorous",
"trusting",
"open",
"thankful",
"radiant",
"adoring",
"passionate"],
"GLAD":[
"happy",
"excited",
"hopeful",
"joyful",
"satisfied",
"delighted",
"encouraged",
"grateful",
"confident",
"inspired",
"touched",
"proud",
"exhilarated",
"ecstatic",
"optimistic",
"glorious"],
"PLAYFUL":[
"energetic",
"effervescent",
"invigorated",
"zestful",
"refreshed",
"impish",
"alive",
"lively",
"exuberant",
"giddy",
"adventurous",
"mischievous",
"jubilant",
"goofy",
"buoyant",
"electrified"],
"INTERESTED":[
"involved",
"inquisitive",
"intense",
"enriched",
"absorbed",
"alert",
"aroused",
"astonished",
"concerned",
"curious",
"eager",
"enthusiastic",
"fascinated",
"intrigued",
"surprised",
"helpful"],
"MAD":[
"impatient",
"pessimistic",
"disgruntled",
"frustrated",
"irritable",
"edgy",
"grouchy",
"agitated",
"exasperated",
"disgusted",
"irked",
"cantankerous",
"animosity",
"bitter",
"rancorous",
"irate",
"furious",
"angry",
"hostile",
"enraged",
"violent"],
"SAD":[
"lonely",
"heavy",
"troubled",
"helpless",
"gloomy",
"overwhelmed",
"distant",
"despondent",
"discouraged",
"distressed",
"dismayed",
"disheartened",
"despairing",
"sorrowful",
"unhappy",
"depressed",
"blue",
"miserable",
"dejected",
"melancholy"],
"SCARED":[
"afraid",
"fearful",
"terrified",
"startled",
"nervous",
"jittery",
"horrified",
"anxious",
"worried",
"anguished",
"lonely",
"insecure",
"sensitive",
"shocked",
"apprehensive",
"dread",
"jealous",
"desperate",
"suspicious",
"frightened"],
"TIRED":[
"exhausted",
"fatigued",
"inert",
"lethargic",
"indifferent",
"weary",
"overwhelmed",
"fidgety",
"helpless",
"heavy",
"sleepy",
"disinterested",
"reluctant",
"passive",
"dull",
"bored",
"listless",
"blah",
"mopey",
"comatose"],
"CONFUSED":[
"frustrated",
"perplexed",
"hesitant",
"troubled",
"uncomfortable",
"withdrawn",
"apathetic",
"embarrassed",
"hurt",
"uneasy",
"irritated",
"suspicious",
"unsteady",
"puzzled",
"restless",
"boggled",
"chagrined",
"unglued",
"detached",
"skeptical"]}

#nuanced_feelings = list(map(str.lower,nuanced_feelings))

pain_joy = ['joy','pain']

body_feelings = ['hungry', 'tired', 'thirsty', 'cold','hot', 'itchy','sick','nauseous', 'urgent', 'bloated','numb','tingly','relieved',
                 'disgust', 'uncomfortable', 'compressed', 'stressed', 'difficulty breathing', 'energetic', 'sore', 'stinging', 'stuffed',
                 '','burning' ]

base_feelings = ['grief','relief', 'sad','angry','mad','confused','hungry','thirsty','warm','hot','cold',
                 'playful','amused','scared','afraid','exhausted','tired','peaceful','calm','tranquil','eager',
                 'excited','aggravated','frustrated','affectionate','appreciative','tender','pain','shame','grateful','anxious','disgust']

my_list = []
for feeling in nuanced_feelings:
    if feeling not in my_list:
        my_list.append(feeling.lower())

#nuanced_feelings = my_list