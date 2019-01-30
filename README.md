# homemade_steganog
```
pip install homemade-steganog
```
Example usage:
```python
import matplotlib.pyplot as plt
from homemade_steganog import Steg

img_path = '../data/img.jpeg'
data_path = '../data/text.txt'
s = Steg()
s.load_img(img_path)
s.load_data(data_path)
data_in_img = s.encrypt()

# Send image here
plt.imshow(data_in_img)
plt.show()
```
![alt text](https://github.com/zoomie/homemade_steg/blob/master/data/img.jpeg)

```python
message = s.decrypt_img(data_in_img)
print(message)
```
# The following text was encoded into the photo show above.

how can entropy be reversed
the last question by isaac asimov 1956

the last question was asked for the first time, half in jest, on may 21, 2061, at a time when humanity first stepped into the light. the question came about as a result of a five dollar bet over highballs, and it happened this way:

alexander adell and bertram lupov were two of the faithful attendants of multivac. as well as any human beings could, they knew what lay behind the cold, clicking, flashing face -- miles and miles of face -- of that giant computer. they had at least a vague notion of the general plan of relays and circuits that had long since grown past the point where any single human could possibly have a firm grasp of the whole.

multivac was self-adjusting and self-correcting. it had to be, for nothing human could adjust and correct it quickly enough or even adequately enough -- so adell and lupov attended the monstrous giant only lightly and superficially, yet as well as any men could. they fed it data, adjusted questions to its needs and translated the answers that were issued. certainly they, and all others like them, were fully entitled to share in the glory that was multivac's.

for decades, multivac had helped design the ships and plot the trajectories that enabled man to reach the moon, mars, and venus, but past that, earth's poor resources could not support the ships. too much energy was needed for the long trips. earth exploited its coal and uranium with increasing efficiency, but there was only so much of both.

but slowly multivac learned enough to answer deeper questions more fundamentally, and on may 14,2061, what had been theory, became fact.

the energy of the sun was stored, converted, and utilized directly on a planet-wide scale. all earth turned off its burning coal, its fissioning uranium, and flipped the switch that connected all of it to a small station, one mile in diameter, circling the earth at half the distance of themoon. all earth ran by invisible beams of sunpower.

seven days had not sufficed to dim the glory of it and adell and lupov finally managed to escapefrom the public function, and to meet in quiet where no one would think of looking for them, in the deserted underground chambers, where portions of the mighty buried body of multivac showed. unattended, idling, sorting data with contented lazy clickings, multivac, too, had earned its vacation and the boys appreciated that. they had no intention, originally, of disturbing it.

they had brought a bottle with them, and their only concern at the moment was to relax in the company of each other and the bottle.

"it's amazing when you think of it," said adell. his broad face had lines of weariness in it, and he stirred his drink slowly with a glass rod, watching the cubes of ice slur clumsily about. "all the energy we can possibly ever use for free. enough energy, if we wanted to draw on it, to melt all earth into a big drop of impure liquid iron, and still never miss the energy so used. all the energy we could ever use, forever and forever and forever."

lupov cocked his head sideways. he had a trick of doing that when he wanted to be contrary, and he wanted to be contrary now, partly because he had had to carry the ice and glassware. "not forever," he said.

"oh, hell, just about forever. till the sun runs down, bert."

"that's not forever."

"all right, then. billions and billions of years. twenty billion, maybe. are you satisfied?"

lupov put his fingers through his thinning hair as though to reassure himself that some was still left and sipped gently at his own drink. "twenty billion years isn't forever."

"will, it will last our time, won't it?"

"so would the coal and uranium."

"all right, but now we can hook up each individual spaceship to the solar station, and it can goto pluto and back a million times without ever worrying about fuel. you can't do that on coal and uranium. ask multivac, if you don't believe me."

"i don't have to ask multivac. i know that."

"then stop running down what multivac's done for us," said adell, blazing up. "it did all right."

"who says it didn't? what i say is that a sun won't last forever. that's all i'm saying. we're safe for twenty billion years, but then what?" lupov pointed a slightly shaky finger at the other."and don't say we'll switch to another sun."

there was silence for a while. adell put his glass to his lips only occasionally, and lupov's eyes slowly closed. they rested.

then lupov's eyes snapped open. "you're thinking we'll switch to another sun when ours is done, aren't you?"

"i'm not thinking."

"sure you are. you're weak on logic, that's the trouble with you. you're like the guy in the story who was caught in a sudden shower and who ran to a grove of trees and got under one. he wasn'tworried, you see, because he figured when one tree got wet through, he would just get under another one."

"i get it," said adell. "don't shout. when the sun is done, the other stars will be gone, too."

"darn right they will," muttered lupov. "it all had a beginning in the original cosmic explosion, whatever that was, and it'll all have an end when all the stars run down. some run down faster than others. hell, the giants won't last a hundred million years. the sun will last twenty billion years and maybe the dwarfs will last a hundred billion for all the good they are. but just giveus a trillion years and everything will be dark. entropy has to increase to maximum, that's all."

"i know all about entropy," said adell, standing on his dignity.

"the hell you do."

"i know as much as you do."

"then you know everything's got to run down someday."

"all right. who says they won't?"

"you did, you poor sap. you said we had all the energy we needed, forever. you said 'forever.'"

"it was adell's turn to be contrary. "maybe we can build things up again someday," he said.

"never."

"why not? someday."

"never."

"ask multivac."

"you ask multivac. i dare you. five dollars says it can't be done."

adell was just drunk enough to try, just sober enough to be able to phrase the necessary symbolsand operations into a question which, in words, might have corresponded to this: will mankind one day without the net expenditure of energy be able to restore the sun to its full youthfulness even after it had died of old age?

or maybe it could be put more simply like this: how can the net amount of entropy of the universe be massively decreased?

multivac fell dead and silent. the slow flashing of lights ceased, the distant sounds of clicking relays ended.

then, just as the frightened technicians felt they could hold their breath no longer, there was a sudden springing to life of the teletype attached to that portion of multivac. five words were printed: insufficient data for meaningful answer.

"no bet," whispered lupov. they left hurriedly.

by next morning, the two, plagued with throbbing head and cottony mouth, had forgotten about theincident.

jerrodd, jerrodine, and jerrodette i and ii watched the starry picture in the visiplate change as the passage through hyperspace was completed in its non-time lapse. at once, the even powderingof stars gave way to the predominance of a single bright marble-disk, centered.

"that's x-23," said jerrodd confidently. his thin hands clamped tightly behind his back and the knuckles whitened.

the little jerrodettes, both girls, had experienced the hyperspace passage for the first time intheir lives and were self-conscious over the momentary sensation of inside-outness. they buried their giggles and chased one another wildly about their mother, screaming, "we've reached x-23 --we've reached x-23 -- we've ----"

"quiet, children," said jerrodine sharply. "are you sure, jerrodd?"

"what is there to be but sure?" asked jerrodd, glancing up at the bulge of featureless metal just under the ceiling. it ran the length of the room, disappearing through the wall at either end. it was as long as the ship.

jerrodd scarcely knew a thing about the thick rod of metal except that it was called a microvac,that one asked it questions if one wished; that if one did not it still had its task of guiding the ship to a preordered destination; of feeding on energies from the various sub-galactic power stations; of computing the equations for the hyperspacial jumps.

jerrodd and his family had only to wait and live in the comfortable residence quarters of the ship.

someone had once told jerrodd that the "ac" at the end of "microvac" stood for "analog computer"in ancient english, but he was on the edge of forgetting even that.

jerrodine's eyes were moist as she watched the visiplate. "i can't help it. i feel funny about leaving earth."

"why for pete's sake?" demanded jerrodd. "we had nothing there. we'll have everything on x-23. you won't be alone. you won't be a pioneer. there are over a million people on the planet already.good lord, our great grandchildren will be looking for new worlds because x-23 will be overcrowded."

then, after a reflective pause, "i tell you, it's a lucky thing the computers worked out interstellar travel the way the race is growing."

"i know, i know," said jerrodine miserably.

jerrodette i said promptly, "our microvac is the best microvac in the world."

"i think so, too," said jerrodd, tousling her hair.

it was a nice feeling to have a microvac of your own and jerrodd was glad he was part of his generation and no other. in his father's youth, the only computers had been tremendous machines taking up a hundred square miles of land. there was only one to a planet. planetary acs they were called. they had been growing in size steadily for a thousand years and then, all at once, came refinement. in place of transistors had come molecular valves so that even the largest planetary ac could be put into a space only half the volume of a spaceship.

jerrodd felt uplifted, as he always did when he thought that his own personal microvac was many times more complicated than the ancient and primitive multivac that had first tamed the sun, and almost as complicated as earth's planetary ac (the largest) that had first solved the problem of hyperspatial travel and had made trips to the stars possible.

"so many stars, so many planets," sighed jerrodine, busy with her own thoughts. "i suppose families will be going out to new planets forever, the way we are now."

"not forever," said jerrodd, with a smile. "it will all stop someday, but not for billions of years. many billions. even the stars run down, you know. entropy must increase."

"what's entropy, daddy?" shrilled jerrodette ii.

"entropy, little sweet, is just a word which means the amount of running-down of the universe. everything runs down, you know, like your little walkie-talkie robot, remember?"

"can't you just put in a new power-unit, like with my robot?"

the stars are the power-units, dear. once they're gone, there are no more power-units."

jerrodette i at once set up a howl. "don't let them, daddy. don't let the stars run down."

"now look what you've done, " whispered jerrodine, exasperated.

"how was i to know it would frighten them?" jerrodd whispered back.

"ask the microvac," wailed jerrodette i. "ask him how to turn the stars on again."

"go ahead," said jerrodine. "it will quiet them down." (jerrodette ii was beginning to cry, also.)

jarrodd shrugged. "now, now, honeys. i'll ask microvac. don't worry, he'll tell us."

he asked the microvac, adding quickly, "print the answer."

jerrodd cupped the strip of thin cellufilm and said cheerfully, "see now, the microvac says it will take care of everything when the time comes so don't worry."

jerrodine said, "and now children, it's time for bed. we'll be in our new home soon."

jerrodd read the words on the cellufilm again before destroying it: insufficient data for a meaningful answer.

he shrugged and looked at the visiplate. x-23 was just ahead.

vj-23x of lameth stared into the black depths of the three-dimensional, small-scale map of the galaxy and said, "are we ridiculous, i wonder, in being so concerned about the matter?"

mq-17j of nicron shook his head. "i think not. you know the galaxy will be filled in five years at the present rate of expansion."

both seemed in their early twenties, both were tall and perfectly formed.

"still," said vj-23x, "i hesitate to submit a pessimistic report to the galactic council."

"i wouldn't consider any other kind of report. stir them up a bit. we've got to stir them up."

vj-23x sighed. "space is infinite. a hundred billion galaxies are there for the taking. more."

"a hundred billion is not infinite and it's getting less infinite all the time. consider! twentythousand years ago, mankind first solved the problem of utilizing stellar energy, and a few centuries later, interstellar travel became possible. it took mankind a million years to fill one small world and then only fifteen thousand years to fill the rest of the galaxy. now the population doubles every ten years --"

vj-23x interrupted. "we can thank immortality for that."

"very well. immortality exists and we have to take it into account. i admit it has its seamy side, this immortality. the galactic ac has solved many problems for us, but in solving the problemsof preventing old age and death, it has undone all its other solutions."

"yet you wouldn't want to abandon life, i suppose."

"not at all," snapped mq-17j, softening it at once to, "not yet. i'm by no means old enough. howold are you?"

"two hundred twenty-three. and you?"

"i'm still under two hundred. --but to get back to my point. population doubles every ten years.once this galaxy is filled, we'll have another filled in ten years. another ten years and we'll have filled two more. another decade, four more. in a hundred years, we'll have filled a thousandgalaxies. in a thousand years, a million galaxies. in ten thousand years, the entire known universe. then what?"

vj-23x said, "as a side issue, there's a problem of transportation. i wonder how many sunpower units it will take to move galaxies of individuals from one galaxy to the next."

"a very good point. already, mankind consumes two sunpower units per year."

"most of it's wasted. after all, our own galaxy alone pours out a thousand sunpower units a yearand we only use two of those."

"granted, but even with a hundred per cent efficiency, we can only stave off the end. our energyrequirements are going up in geometric progression even faster than our population. we'll run out of energy even sooner than we run out of galaxies. a good point. a very good point."

"we'll just have to build new stars out of interstellar gas."

"or out of dissipated heat?" asked mq-17j, sarcastically.

"there may be some way to reverse entropy. we ought to ask the galactic ac."

vj-23x was not really serious, but mq-17j pulled out his ac-contact from his pocket and placed it on the table before him.

"i've half a mind to," he said. "it's something the human race will have to face someday."

he stared somberly at his small ac-contact. it was only two inches cubed and nothing in itself, but it was connected through hyperspace with the great galactic ac that served all mankind. hyperspace considered, it was an integral part of the galactic ac.

mq-17j paused to wonder if someday in his immortal life he would get to see the galactic ac. it was on a little world of its own, a spider webbing of force-beams holding the matter within whichsurges of sub-mesons took the place of the old clumsy molecular valves. yet despite it's sub-etheric workings, the galactic ac was known to be a full thousand feet across.

mq-17j asked suddenly of his ac-contact, "can entropy ever be reversed?"

vj-23x looked startled and said at once, "oh, say, i didn't really mean to have you ask that."

"why not?"

"we both know entropy can't be reversed. you can't turn smoke and ash back into a tree."

"do you have trees on your world?" asked mq-17j.

the sound of the galactic ac startled them into silence. its voice came thin and beautiful out of the small ac-contact on the desk. it said: there is insufficient data for a meaningful answer.

vj-23x said, "see!"

the two men thereupon returned to the question of the report they were to make to the galactic council.

zee prime's mind spanned the new galaxy with a faint interest in the countless twists of stars that powdered it. he had never seen this one before. would he ever see them all? so many of them, each with its load of humanity - but a load that was almost a dead weight. more and more, the real essence of men was to be found out here, in space.

minds, not bodies! the immortal bodies remained back on the planets, in suspension over the eons. sometimes they roused for material activity but that was growing rarer. few new individuals were coming into existence to join the incredibly mighty throng, but what matter? there was little room in the universe for new individuals.

zee prime was roused out of his reverie upon coming across the wispy tendrils of another mind.

"i am zee prime," said zee prime. "and you?"

"i am dee sub wun. your galaxy?"

"we call it only the galaxy. and you?"

"we call ours the same. all men call their galaxy their galaxy and nothing more. why not?"

"true. since all galaxies are the same."

"not all galaxies. on one particular galaxy the race of man must have originated. that makes it different."

zee prime said, "on which one?"

"i cannot say. the universal ac would know."

"shall we ask him? i am suddenly curious."

zee prime's perceptions broadened until the galaxies themselves shrunk and became a new, more diffuse powdering on a much larger background. so many hundreds of billions of them, all with theirimmortal beings, all carrying their load of intelligences with minds that drifted freely throughspace. and yet one of them was unique among them all in being the originals galaxy. one of them had, in its vague and distant past, a period when it was the only galaxy populated by man.

zee prime was consumed with curiosity to see this galaxy and called, out: "universal ac! on which galaxy did mankind originate?"

the universal ac heard, for on every world and throughout space, it had its receptors ready, andeach receptor lead through hyperspace to some unknown point where the universal ac kept itself aloof.

zee prime knew of only one man whose thoughts had penetrated within sensing distance of universal ac, and he reported only a shining globe, two feet across, difficult to see.

"but how can that be all of universal ac?" zee prime had asked.

"most of it, " had been the answer, "is in hyperspace. in what form it is there i cannot imagine."

nor could anyone, for the day had long since passed, zee prime knew, when any man had any part of the making of a universal ac. each universal ac designed and constructed its successor. each, during its existence of a million years or more accumulated the necessary data to build a better and more intricate, more capable successor in which its own store of data and individuality would be submerged.

the universal ac interrupted zee prime's wandering thoughts, not with words, but with guidance. zee prime's mentality was guided into the dim sea of galaxies and one in particular enlarged intostars.

a thought came, infinitely distant, but infinitely clear. "this is the original galaxy of man."

but it was the same after all, the same as any other, and zee prime stifled his disappointment.

dee sub wun, whose mind had accompanied the other, said suddenly, "and is one of these stars theoriginal star of man?"

the universal ac said, "man's original star has gone nova. it is now a white dwarf."

"did the men upon it die?" asked zee prime, startled and without thinking.

the universal ac said, "a new world, as in such cases, was constructed for their physical bodiesin time."

"yes, of course," said zee prime, but a sense of loss overwhelmed him even so. his mind releasedits hold on the original galaxy of man, let it spring back and lose itself among the blurred pinpoints. he never wanted to see it again.

dee sub wun said, "what is wrong?"

"the stars are dying. the original star is dead."

"they must all die. why not?"

"but when all energy is gone, our bodies will finally die, and you and i with them."

"it will take billions of years."

"i do not wish it to happen even after billions of years. universal ac! how may stars be kept from dying?"

dee sub wun said in amusement, "you're asking how entropy might be reversed in direction."

and the universal ac answered. "there is as yet insufficient data for a meaningful answer."

zee prime's thoughts fled back to his own galaxy. he gave no further thought to dee sub wun, whose body might be waiting on a galaxy a trillion light-years away, or on the star next to zee prime's own. it didn't matter.

unhappily, zee prime began collecting interstellar hydrogen out of which to build a small star of his own. if the stars must someday die, at least some could yet be built.

man considered with himself, for in a way, man, mentally, was one. he consisted of a trillion, trillion, trillion ageless bodies, each in its place, each resting quiet and incorruptible, each cared for by perfect automatons, equally incorruptible, while the minds of all the bodies freely melted one into the other, indistinguishable.

man said, "the universe is dying."

man looked about at the dimming galaxies. the giant stars, spendthrifts, were gone long ago, back in the dimmest of the dim far past. almost all stars were white dwarfs, fading to the end.

new stars had been built of the dust between the stars, some by natural processes, some by man himself, and those were going, too. white dwarfs might yet be crashed together and of the mighty forces so released, new stars built, but only one star for every thousand white dwarfs destroyed, and those would come to an end, too.

man said, "carefully husbanded, as directed by the cosmic ac, the energy that is even yet left in all the universe will last for billions of years."

"but even so," said man, "eventually it will all come to an end. however it may be husbanded, however stretched out, the energy once expended is gone and cannot be restored. entropy must increase to the maximum."

man said, "can entropy not be reversed? let us ask the cosmic ac."

the cosmic ac surrounded them but not in space. not a fragment of it was in space. it was in hyperspace and made of something that was neither matter nor energy. the question of its size and nature no longer had meaning to any terms that man could comprehend.

"cosmic ac," said man, "how may entropy be reversed?"

the cosmic ac said, "there is as yet insufficient data for a meaningful answer."

man said, "collect additional data."

the cosmic ac said, "i will do so. i have been doing so for a hundred billion years. my predecessors and i have been asked this question many times. all the data i have remains insufficient."

"will there come a time," said man, "when data will be sufficient or is the problem insoluble inall conceivable circumstances?"

the cosmic ac said, "no problem is insoluble in all conceivable circumstances."

man said, "when will you have enough data to answer the question?"

"there is as yet insufficient data for a meaningful answer."

"will you keep working on it?" asked man.

the cosmic ac said, "i will."

man said, "we shall wait."

"the stars and galaxies died and snuffed out, and space grew black after ten trillion years of running down.

one by one man fused with ac, each physical body losing its mental identity in a manner that wassomehow not a loss but a gain.

man's last mind paused before fusion, looking over a space that included nothing but the dregs of one last dark star and nothing besides but incredibly thin matter, agitated randomly by the tagends of heat wearing out, asymptotically, to the absolute zero.

man said, "ac, is this the end? can this chaos not be reversed into the universe once more? can that not be done?"

ac said, "there is as yet insufficient data for a meaningful answer."

man's last mind fused and only ac existed -- and that in hyperspace.

matter and energy had ended and with it, space and time. even ac existed only for the sake of the one last question that it had never answered from the time a half-drunken computer ten trillionyears before had asked the question of a computer that was to ac far less than was a man to man.

all other questions had been answered, and until this last question was answered also, ac might not release his consciousness.

all collected data had come to a final end. nothing was left to be collected.

but all collected data had yet to be completely correlated and put together in all possible relationships.

a timeless interval was spent in doing that.

and it came to pass that ac learned how to reverse the direction of entropy.

but there was now no man to whom ac might give the answer of the last question. no matter. the answer -- by demonstration -- would take care of that, too.

for another timeless interval, ac thought how best to do this. carefully, ac organized the program.

the consciousness of ac encompassed all of what had once been a universe and brooded over what was now chaos. step by step, it must be done.

and ac said, "let there be light!"

and there was light----


back to multivax