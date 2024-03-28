Tasks = [
    {
        'Task': 'Task 1', 
        'Section': 'Reasoning',
        'Header1': 'Each question in this section consists of a short statement and a following question.',
        'Header2': 'After you3 have memorized the statement, click the right arrow [or slied] to reveal the question itself.'
     },
    {
        'Task': 'Task 2', 
        'Section': 'Perceptual Speed',
        'Header1': 'Each question in this section consists of a short statement and a following question.',
        'Header2': 'After you have memorized the statement, click the right arrow [or slied] to reveal the question itself.'
     },    
    {
        'Task': 'Task 3', 
        'Section': 'Number Speed and Accuracy',
        'Header1': 'Each question in this section consists of a short statement and a following question.',
        'Header2': 'After you have memorized the statement, click the right arrow [or slied] to reveal the question itself.'
     },
    {
        'Task': 'Task 4', 
        'Section': 'Word Meaning',
        'Header1': 'Each question in this section consists of a short statement and a following question.',
        'Header2': 'After you have memorized the statement, click the right arrow [or slied] to reveal the question itself.'
     },    
    {
        'Task': 'Task 5', 
        'Section': 'Spatial Visualization',
        'Header1': 'Each question in this section consists of a short statement and a following question.',
        'Header2': 'After you have memorized the statement, click the right arrow [or slied] to reveal the question itself.'
     },    
]

Line2 = 'Work as quickly and accurately ass possible.'
Line3 = 'Good luck!'

# TASK 1
reasoning_pairs = [
    {'Statement': 'Jack is taller than James', 'Question': 'Who is shorter?','Choices': ['Jack', 'James'], 'Answer': 'James'},
    {'Statement': 'Ruth is not as old as Lily', 'Question': 'Who is older?', 'Choices': ['Ruth', 'Lily'], 'Answer': 'Lily'},
    {'Statement': 'Mark is heavier than David', 'Question': 'Who is heavier?', 'Choices': ['David', 'Mark'], 'Answer': 'Mark'},
    {'Statement': 'Emma is poorer than Bruce', 'Question': 'Who is richer?','Choices': ['Bruce', 'Emma'], 'Answer': 'Bruce'},
    {'Statement': 'Lee is stronger than Josh', 'Question': 'Who is weaker?','Choices': ['Josh', 'Lee'], 'Answer': 'Josh'},
    {'Statement': 'Todd is not as funny as Matt', 'Question': 'Who is funnier?', 'Choices': ['Todd', 'Matt'], 'Answer': 'Matt'},
    {'Statement': 'Mike is not as sad as Stacy', 'Question': 'Who is happier?', 'Choices': ['Stacy', 'Mike'], 'Answer': 'Mike'},
    {'Statement': 'Ron is smarter than Joe', 'Question': 'Who is less smart?', 'Choices': ['Joe', 'Ron'], 'Answer': 'Joe'},
    {'Statement': 'Alice is taller than Bob', 'Question': 'Who is shorter?', 'Choices': ['Alice', 'Bob'], 'Answer': 'Bob'},
    {'Statement': 'Sara is older than Emily', 'Question': 'Who is younger?', 'Choices': ['Emily', 'Sara'], 'Answer': 'Emily'},
    {'Statement': 'John is heavier than Michael', 'Question': 'Who is lighter?', 'Choices': ['Michael', 'John'], 'Answer': 'Michael'},
    {'Statement': 'Anna is richer than Kate', 'Question': 'Who is poorer?', 'Choices': ['Kate', 'Anna'], 'Answer': 'Kate'},
    {'Statement': 'Chris is stronger than Peter', 'Question': 'Who is weaker?', 'Choices': ['Peter', 'Chris'], 'Answer': 'Peter'},
    {'Statement': 'Linda is funnier than Carol', 'Question': 'Who is less funny?', 'Choices': ['Carol', 'Linda'], 'Answer': 'Carol'},
    {'Statement': 'Greg is happier than Paul', 'Question': 'Who is sadder?', 'Choices': ['Paul', 'Greg'], 'Answer': 'Paul'},
    {'Statement': 'Mary is smarter than Lisa', 'Question': 'Who is less smart?', 'Choices': ['Lisa', 'Mary'], 'Answer': 'Lisa'},
    {'Statement': 'Tom is taller than Tim', 'Question': 'Who is shorter?', 'Choices': ['Tom', 'Tim'], 'Answer': 'Tim'},
    {'Statement': 'Hannah is older than Emma', 'Question': 'Who is younger?', 'Choices': ['Emma', 'Hannah'], 'Answer': 'Emma'},
    {'Statement': 'Richard is heavier than Daniel', 'Question': 'Who is lighter?', 'Choices': ['Daniel', 'Richard'], 'Answer': 'Daniel'},
    {'Statement': 'Sophia is richer than Olivia', 'Question': 'Who is poorer?', 'Choices': ['Olivia', 'Sophia'], 'Answer': 'Olivia'},
    {'Statement': 'Lucas is stronger than Ethan', 'Question': 'Who is weaker?', 'Choices': ['Ethan', 'Lucas'], 'Answer': 'Ethan'},
    {'Statement': 'Rachel is funnier than Jessica', 'Question': 'Who is less funny?', 'Choices': ['Jessica', 'Rachel'], 'Answer': 'Jessica'},
    {'Statement': 'Ben is happier than Andrew', 'Question': 'Who is sadder?', 'Choices': ['Andrew', 'Ben'], 'Answer': 'Andrew'},
    {'Statement': 'Grace is smarter than Emily', 'Question': 'Who is less smart?', 'Choices': ['Emily', 'Grace'], 'Answer': 'Emily'},
    {'Statement': 'Dylan is taller than Logan', 'Question': 'Who is shorter?', 'Choices': ['Logan', 'Dylan'], 'Answer': 'Logan'},
    {'Statement': 'Madison is older than Chloe', 'Question': 'Who is younger?', 'Choices': ['Chloe', 'Madison'], 'Answer': 'Chloe'},
    {'Statement': 'Nathan is heavier than Ethan', 'Question': 'Who is lighter?', 'Choices': ['Ethan', 'Nathan'], 'Answer': 'Ethan'},
    {'Statement': 'Ava is richer than Mia', 'Question': 'Who is poorer?', 'Choices': ['Mia', 'Ava'], 'Answer': 'Mia'},
    {'Statement': 'Peter is not as big as John', 'Question': 'Who is smaller?', 'Choices': ['Peter', 'John'], 'Answer': 'Peter'},
    {'Statement': 'Alice is not as tall as Bob', 'Question': 'Who is shorter?', 'Choices': ['Alice', 'Bob'], 'Answer': 'Alice'},
    {'Statement': 'Sara is not as fast as Emily', 'Question': 'Who is slower?', 'Choices': ['Sara', 'Emily'], 'Answer': 'Sara'},
    {'Statement': 'Michael is not as strong as David', 'Question': 'Who is weaker?', 'Choices': ['Michael', 'David'], 'Answer': 'Michael'},
    {'Statement': 'Sophia is not as smart as Olivia', 'Question': 'Who is less smart?', 'Choices': ['Sophia', 'Olivia'], 'Answer': 'Sophia'},
    {'Statement': 'Ethan is not as good at singing as Lucas', 'Question': 'Who is worse at singing?', 'Choices': ['Ethan', 'Lucas'], 'Answer': 'Ethan'},
    {'Statement': 'Lily is not as good at drawing as Emma', 'Question': 'Who is worse at drawing?', 'Choices': ['Lily', 'Emma'], 'Answer': 'Lily'},
    {'Statement': 'Chloe is not as talented as Madison', 'Question': 'Who is the more skillful?', 'Choices': ['Madison', 'Chloe'], 'Answer': 'Madison'},
    {'Statement': 'Juan is running faster than Tim', 'Question': 'Who will probably win the race?', 'Choices': ['Juan', 'Tim'], 'Answer': 'Juan'},
    {'Statement': 'Lucia does not play piano as well as Emma', 'Question': 'Who is the piano teacher?', 'Choices': ['Emma', 'Lucia'], 'Answer': 'Emma'},
    {'Statement': 'Peter is wiser than Daniel', 'Question': 'Who is the dumbest oen?', 'Choices': ['Daniel', 'Peter'], 'Answer': 'Daniel'},
    {'Statement': 'Ernesto is more talktative than Olivia', 'Question': 'Who is more reserved?', 'Choices': ['Olivia', 'Ernesto'], 'Answer': 'Olivia'},
    {'Statement': 'Melania dances better than Silvia', 'Question': 'Who is a bad dancer?', 'Choices': ['Silvia', 'Melania'], 'Answer': 'Silvia'},
    {'Statement': 'Ethan is not as good at singing as Lucas', 'Question': 'Who is worse at singing?', 'Choices': ['Ethan', 'Lucas'], 'Answer': 'Ethan'},
    {'Statement': 'Lily is not as good at drawing as Emma', 'Question': 'Who is worse at drawing?', 'Choices': ['Lily', 'Emma'], 'Answer': 'Lily'},
    {'Statement': 'Chloe is not as talented as Madison', 'Question': 'Who is the more skillful?', 'Choices': ['Madison', 'Chloe'], 'Answer': 'Madison'},    
    {'Statement': 'Ethan is not as good at singing as Lucas', 'Question': 'Who is worse at singing?', 'Choices': ['Ethan', 'Lucas'], 'Answer': 'Ethan'},
    {'Statement': 'Lily is not as good at drawing as Emma', 'Question': 'Who is worse at drawing?', 'Choices': ['Lily', 'Emma'], 'Answer': 'Lily'},
    {'Statement': 'Chloe is not as talented as Madison', 'Question': 'Who is the more skillful?', 'Choices': ['Madison', 'Chloe'], 'Answer': 'Madison'},  
]

# TASK 2
perceptual_top = ['E', 'Q', 'D', 'K', 'R', 'P']


synonym_pairs = [
    ['happy', 'joyful'], ['sad', 'gloomy'], ['big', 'large'], ['small', 'tiny'], ['hot', 'burning'], ['cold', 'freezing'], ['teach', 'educate'], ['learn', 'study'], 
    ['break', 'shatter'], ['fix', 'repair'], ['day', 'morning'], ['night', 'evening'], ['give', 'donate'], ['take', 'receive'], ['sharp', 'keen'], ['dull', 'blunt'], 
    ['high', 'tall'], ['low', 'short'], ['red', 'crimson'], ['blue', 'azure'], ['green', 'emerald'], ['yellow', 'golden'], ['black', 'dark'], ['white', 'pale'], 
    ['walk', 'run'], ['talk', 'shout'], ['write', 'draw'], ['read', 'watch'], ['eat', 'drink'], ['think', 'ponder'], ['dog', 'puppy'], ['bird', 'fly'], 
    ['horse', 'mare'], ['snake', 'serpent'], ['elephant', 'giant'], ['monkey', 'ape'], ['house', 'building'], ['car', 'vehicle'], ['book', 'magazine'], 
    ['table', 'desk'], ['computer', 'laptop'], ['door', 'gateway'], ['bread', 'loaf'], ['cheese', 'dairy'], ['meat', 'flesh'], ['vegetables', 'greens'], 
    ['pasta', 'noodles'], ['candy', 'sweets'], ['angry', 'furious'], ['scared', 'terrified'], ['tired', 'weary'], ['bored', 'monotonous'], ['proud', 'elated'], 
    ['jealous', 'envious'], ['speak', 'converse'], ['whisper', 'murmur'], ['bright', 'luminous'], ['dull', 'lifeless'], ['loud', 'boisterous'], ['quiet', 'silent'], 
    ['fragrant', 'aromatic'], ['foul', 'putrid'], ['heavy', 'weighty'], ['light', 'airy'], ['abundant', 'plentiful'], ['scarce', 'rare'], ['victory', 'triumph'], 
    ['defeat', 'loss'], ['hope', 'optimism'], ['despair', 'despondency'], ['love', 'affection'], ['hate', 'loathing'], ['trust', 'reliance'], ['betrayal', 'treachery']
 ]

antonym_pairs = [
    ['happy', 'sad'], ['big', 'small'], ['hot', 'cold'], ['long', 'short'], ['wide', 'narrow'], ['bright', 'dark'], ['rough', 'smooth'], ['wet', 'dry'],
    ['loud', 'quiet'], ['fast', 'slow'], ['deep', 'shallow'],['thick', 'thin'], ['heavy', 'light'], ['full', 'empty'], ['open', 'closed'], ['clean', 'dirty'],
    ['strong', 'weak'], ['beautiful', 'ugly'], ['rich', 'poor'], ['young', 'old'], ['active', 'passive'], ['kind', 'cruel'], ['honest', 'dishonest'], ['brave', 'cowardly'],
    ['careful', 'careless'], ['optimistic', 'pessimistic'], ['generous', 'selfish'], ['polite', 'rude'], ['calm', 'angry'], ['peaceful', 'chaotic'], ['healthy', 'sick'], ['fresh', 'stale'],
    ['sweet', 'sour'], ['bitter', 'sweet'], ['soft', 'hard'], ['smooth', 'rough'], ['flexible', 'rigid'], ['dull', 'sharp'], ['loud', 'quiet'], ['noisy', 'silent'], ['fragrant', 'smelly'],
    ['attractive', 'unattractive'], ['successful', 'unsuccessful'], ['winner', 'loser'], ['gain', 'lose'], ['beginning', 'end'], ['top', 'bottom'], ['front', 'back'],  ['inside', 'outside'],
    ['above', 'below'], ['speak', 'listen'], ['give', 'take'], ['buy', 'sell'], ['show', 'hide'], ['open', 'close'], ['build', 'destroy'], ['create', 'destroy'],
    ['start', 'finish'], ['arrive', 'leave'], ['come', 'go'], ['day', 'night'], ['summer', 'winter'], ['hot', 'cold'], ['dry', 'wet'], ['light', 'dark'],
    ['love', 'hate'], ['trust', 'doubt'], ['friend', 'enemy'], ['truth', 'lie'], ['justice', 'injustice'],['freedom', 'imprisonment'], ['peace', 'war'], ['order', 'chaos'], 
    ['success', 'failure'], ['victory', 'defeat'], ['knowledge', 'ignorance'], ['wisdom', 'foolishness'], ['logic', 'emotion'], ['science', 'faith'], ['reality', 'fantasy'],  ['simple', 'complex'],
    ['easy', 'difficult'], ['familiar', 'strange'], ['famous', 'unknown'], ['public', 'private'], ['open', 'secret'], ['honest', 'deceitful'], ['clear', 'unclear'], ['confident', 'unsure'], 
    ['brave', 'cowardly'], ['generous', 'selfish'], ['active', 'lazy'], ['calm', 'excited'], ['patient', 'impatient'], ['organized', 'messy'], ['hopeful', 'despairing'], ['confident', 'doubtful'], 
    ['realistic', 'idealistic'], ['outgoing', 'shy'], ['talkative', 'quiet'],
]

analog_pairs = [
    ['happy', 'joyful'], ['big', 'large'], ['hot', 'burning'], ['long', 'extensive'], ['wide', 'broad'], ['bright', 'brilliant'], ['rough', 'uneven'], ['wet', 'damp'],
    ['loud', 'boisterous'], ['fast', 'rapid'], ['deep', 'profound'], ['thick', 'dense'], ['heavy', 'weighty'], ['full', 'brimming'], ['open', 'uncovered'], ['clean', 'spotless'],
    ['strong', 'powerful'], ['beautiful', 'gorgeous'], ['rich', 'wealthy'], ['young', 'youthful'], ['active', 'energetic'], ['kind', 'benevolent'], ['honest', 'truthful'], ['brave', 'courageous'],
    ['careful', 'cautious'], ['optimistic', 'hopeful'], ['generous', 'unselfish'], ['polite', 'courteous'], ['calm', 'serene'], ['peaceful', 'tranquil'], ['healthy', 'fit'], ['fresh', 'new'],
    ['sweet', 'luscious'], ['bitter', 'acrid'], ['soft', 'gentle'], ['smooth', 'sleek'], ['flexible', 'pliable'], ['dull', 'blunt'], ['noisy', 'raucous'], ['fragrant', 'aromatic'], 
    ['attractive', 'appealing'], ['successful', 'victorious'], ['winner', 'champion'], ['gain', 'acquire'], ['beginning', 'commencement'], ['top', 'summit'], ['front', 'forefront'], ['inside', 'interior'],
    ['above', 'superior'], ['speak', 'converse'], ['give', 'bestow'], ['buy', 'purchase'], ['show', 'display'], ['open', 'unfold'], ['build', 'construct'], ['create', 'fashion'],
    ['start', 'initiate'], ['arrive', 'reach'], ['come', 'approach'], ['day', 'dawn'], ['summer', 'estivation'],  ['love', 'adoration'], ['trust', 'faith'], ['friend', 'companion'],
    ['truth', 'veracity'], ['justice', 'equity'], ['freedom', 'liberty'], ['peace', 'harmony'], ['order', 'method'], ['success', 'achievement'], ['victory', 'triumph'], ['knowledge', 'erudition'],
    ['wisdom', 'sagacity'], ['logic', 'reason'], ['science', 'inquiry'], ['reality', 'actuality'], ['simple', 'basic'], ['easy', 'effortless'], ['familiar', 'well-known'], ['famous', 'renowned'],
    ['public', 'open'], ['open', 'frank'], ['honest', 'sincere'], ['clear', 'unambiguous'], ['confident', 'assured'], ['brave', 'valorous'], ['generous', 'charitable'], ['active', 'dynamic'],
    ['calm', 'composed'], ['patient', 'forbearing'], ['organized', 'systematic'], ['hopeful', 'optimistic'],  ['confident', 'self-assured'], ['realistic', 'pragmatic'], ['outgoing', 'extroverted'],
    ['talkative', 'loquacious'],
]

unrelated_words = [
    'apple', 'chair', 'ocean', 'mountain', 'umbrella', 'piano', 'cloud', 'camera', 'guitar', 'bicycle', 
    'flower', 'river', 'hat', 'moon', 'star', 'candle', 'island', 'mirror', 'sun', 'train',
    'shoe', 'key', 'window', 'ship', 'butterfly', 'wallet', 'globe', 'clock', 'map', 'cake',
    'painting', 'telephone', 'coin', 'hammer', 'chair', 'bag', 'glasses', 'guitar', 'scissors', 'towel',
    'basket', 'pillow', 'mirror', 'cushion', 'bottle', 'gloves', 'book', 'umbrella', 'basketball', 'guitar',
    'brush', 'remote', 'pen', 'lamp', 'fan', 'toothbrush', 'flag', 'mug', 'chair', 'eraser',
    'calculator', 'stapler', 'magnet', 'fridge', 'calendar', 'clock', 'tape', 'wallet', 'sponge', 'microscope', 
    'soul', 'CAT-scan', 'chill', 'vodka'
]

word_pairs = synonym_pairs + antonym_pairs + analog_pairs
