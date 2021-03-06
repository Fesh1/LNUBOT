# connection credentials
DB_URL = ''
# admin password
password = ''
admins_id = []
# entities properties
# date of birth format
DATE_FORMAT = '%d.%m.%Y %H:%M'


TOKEN = ''

faculties = ["bioweb", "geography", "geology", "econom",
              "electronics", "journ", "lingua", "clio",
              "kultart", "mmf","intrel", "pedagogy", "ami", "financial",
             "physics", 'philology', "filos", "chem", "law"]

faculties_url = {"bioweb": 'Біологічний факультет', "geography": 'Географічний факультет',
             "geology": 'Геологічний факультет', "econom": 'Економічний факультет',
              "electronics": 'Факультет електроніки та комп’ютерних технологій',
             "journ": 'Факультет журналістики', "lingua": 'Факультет іноземних мов',
             "clio": 'Історичний факультет',
              "kultart": 'Факультет культури і мистецтв',"mmf": 'Механіко-математичний факультет мехмат',
             "intrel": 'Факультет міжнародних відносин міжнар', "pedagogy": 'Факультет педагогічної освіти педагогіка',
             "ami": 'Факультет прикладної математики та інформатики прикладна',
             "financial": 'Факультет управління фінансами та бізнесу фінанси',
             "physics": 'Фізичний факультет фізфак', 'philology': 'Філологічний факультет філфак',
             "filos": 'Філософський факультет', "chem": 'Хімічний факультет хімфак', "law": 'Юридичний факультет юрфак'}

departments = {'bioweb': ['biophysics-and-bioinformatics',
  'biochemistry',
  'botany',
  'genetics-and-biotechnology',
  'ecology',
  'zoology',
  'microbiology',
  'human-and-animals-psysiology',
  'plant-physiology-and-ecology'],
 'geography': ['geographyofukraine',
  'geomorphologyandpaleogeography',
  'kafedra-gruntoznavstva-i-heohrafiji-gruntiv',
  'ekonomichnoji-i-sotsialnoji-heohrafiji',
  'konstruktyvnoji-heohrafiji-i-kartohrafiji',
  'ratsionalnoho-vykorystannya-pryrodnyh-resursiv-i-ohorony-pryrody',
  'turyzmu',
  'fizychnoji-heohrafiji'],
               'geology': ['kafedra-heolohiji-korysnyh-kopalyn',
  'kafedra-ekolohichnoji-ta-inzhenernoji-heolohiji-i-hidroheolohiji',
  'kafedra-zahalnoji-ta-rehionalnoji-heolohiji',
  'kafedra-mineralohiji'],
               'econom': ['ananalitychnoji-ekonomiji-ta-mizhnarodnoji-ekonomiky',
  'bankivskoho-i-strahovoho-biznesu',
  'economiky-pidpryemstva',
  'ekonomiky-ukrajiny',
  'economic-cybernetics',
  'ekonomichnoji-teoriji',
  'informatsijnyh-system-u-menedzhmenti',
  'marketynhu',
  'menedzhmentu',
  'obliku-i-audytu',
  'statystyky',
  'finansiv-hroshovoho-obihu-ta-kredytu'],
               'electronics': ['optoelectronics-2',
  'radioelectronics-and-computer-sciences',
  'radiophysics-and-computer-technologies',
  'sensor-and-semiconductor-electronics',
  'system-design',
  'physic-and-bioelectronics'],
               'journ': ['kafedra-zarubizhnoji-presy-ta-informatsiji',
  'kafedra-movy-zasobiv-masovoji-informatsiji',
  'kafedra-novyh-medij',
  'kafedra-padiomovlennya-i-telebachennya',
  'kafedra-teoriji-i-praktyky-zhurnalistyky',
  'kafedra-ukrajinskoji-presy'],
               'lingua': ['kafedra-anhlijskoji-filolohiji',
  'inozemnyh-mov-dlya-humanitarnyh-fakultetiv',
  'inozemnyh-mov-dlya-pryrodnychyh-fakultetiv',
  'klasychnoji-filolohiji',
  'mizhkulturnoji-komunikatsiji-ta-perekladu',
  'nimetskoji-filolohiji',
  'the-hryhoriy-kochur-department-of-translation-studies-and-contrastive-linguistics',
  'svitovoji-literatury',
  'frantsuzkoji-filolohiji'],
               'clio': ['sotsiolohiji',
  'arheolohiji-ta-spetsialnyh-haluzej-istorychnoji-nauky',
  'davnoji-istoriji-ukrajiny-ta-arhivoznavstva',
  'etnolohiji',
  'istorychnoho-krajeznavstva',
  'istoriji-serednih-vikiv-ta-vizantynistyky',
  'istoriji-tsentralnoji-ta-shidnoji-evropy',
  'novitnoji-istoriji-ukrajiny',
  'novoji-ta-novitnoji-istoriji-zarubizhnyh-krajin'],
               'kultart': ['bibliotekoznavstva-i-bibliohrafiji',
  'muzykoznavstva',
  'muzychnoho-mystetstva',
  'rezhysury-ta-khoreohrafii',
  'teatroznavstva-ta-aktorskoji-majsternosti',
  'filosofiji-mystetstv'],
               'mmf': ['algebra-and-logic',
  'kvm',
  'heometriji-i-topolohiji',
  'matematychnoho-i-funktsionalnoho-analizu',
  'matematychnoho-modelyuvannya',
  'matematychnoji-ekonomiky-ta-ekonometriji',
  'msde',
  'mehaniky',
  'teoriji-funktsij-i-teoriji-jmovirnostej'],
               'intrel': ['jevropejskoho-prava',
  'inozemnyh-mov',
  'krajinoznavstva-i-mizhnarodnoho-turyzmu',
  'mizhnarodnyh-vidnosyn-i-dyplomatychnoji-sluzhby',
  'mizhnarodnyh-ekonomichnyh-vidnosyn',
  'mizhnarodnoho-ekonomichnoho-analizu-i-finansiv',
  'mizhnarodnoho-prava'],
               'pedagogy': ['pedagogy',
  'kafedra-pochatkovoji-ta-doshkilnoji-osvity',
  'kafedra-korektsijnoji-pedahohiky-ta-inklyuziji'],
               'ami': ['discrete-analysis-intelligent-system',
  'information-systems',
  'mathematical-modeling-of-social-and-economics-processes',
  'computational-mathematics',
  'applied-mathematics',
  'programming',
  'optimal-process-theory'],
               'financial': ['ekonomiky-ta-publichnoho-upravlinnya',
  'obliku-analizu-i-kontrolyu',
  'publichnoho-administruvannya-ta-upravlinnya-biznesom',
  'finansovoho-menedzhmentu',
  'tsyfrovoyi-ekonomiky-ta-biznes-analityky'],
               'physics': ['kafedra-astrofizyky',
  'kafedra-eksperymentalnoji-fizyky',
  'kafedra-zahalnoji-fizyky',
  'kafedra-teoretychnoji-fizyky',
  'fizyky-metaliv',
  'fizyky-tverdogo-tila'],
               'philology': ['zahalnoho-movoznavstva',
  'polskoji-filolohiji',
  'slovyanskoji-filolohiji',
  'shodoznavstva-imeni-profesora-yaroslava-dashkevycha',
  'teoriji-literatury-ta-porivnyalnoho-literaturoznavstva',
  'ukrajinskoho-prykladnoho-movoznavstva',
  'kafedra-ukrajinskoji-literatury-imeni-akademika-myhajla-voznyaka',
  'ukrajinskoji-movy',
  'kafedra-ukrajinskoji-folklorystyky-imeni-akademika-filareta-kolessy'],
               'filos': ['history-of-philosophy',
  'politilogy',
  'psyholohiji',
  'teoriji-ta-istoriji-kultury',
  'https-www-facebook-com-teoryandhistorypoliticalscience',
  'filosofiji'],
               'chem': ['analitycal-chemistry',
  'inorganic-chemistry',
  'organic-chemistry',
  'physical-and-colloid-chemistry'],
               'law': ['administratyvnoho-ta-finansovoho-prava',
  'intelektualnoji-vlasnosti-ta-korporatyvnoho-prava',
  'kafedra-istoriji-derzhavy-prava-ta-polityko-pravovyh-uchen',
  'kafedra-konstytutsijnoho-prava',
  'kafedra-kryminalnoho-prava-ta-kryminolohiji',
  'kafedra-kryminalnoho-protsesu-i-kryminalistyky',
  'kafedra-osnov-prava-ukrajiny',
  'kafedra-soc-prava',
  'kafedra-teoriji-ta-filosofiji-prava',
  'kafedra-cyvilnogo-prava-ta-procesy']}



