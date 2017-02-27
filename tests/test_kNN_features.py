import unittest

from feature_extraction import kNN

class KNNFeaturesTests(unittest.TestCase):

    def setUp(self):
        self.features = []
        self.trace = [[3.46271014214, -1], [3.75556516647, -1], [3.77688622475, 1], [3.77697610855, 1], [3.77704119682, 1], [3.77706813812, 1], [4.35218405724, -1], [4.60580420494, -1], [4.74438214302, -1], [5.13719010353, -1], [5.38602113724, -1], [5.39304900169, -1], [5.39319300652, -1], [5.39908599854, -1], [5.39921808243, -1], [5.39986419678, -1], [5.39998316765, -1], [5.40004205704, -1], [5.4000980854, -1], [5.4001531601, -1], [5.40020918846, -1], [5.40030407906, -1], [5.40404200554, -1], [5.40422701836, -1], [5.40428709984, -1], [5.40435409546, -1], [5.40440917015, -1], [5.40446400642, -1], [5.40451812744, -1], [5.40461111069, -1], [5.41293215752, 1], [5.41308021545, 1], [5.41315817833, 1], [5.41348218918, 1], [5.41358017921, 1], [5.41364216805, 1], [5.43573617935, 1], [5.43591308594, 1], [5.43617105484, 1], [5.4362680912, 1], [5.52504706383, -1], [5.52520108223, -1], [5.52527403831, -1], [5.52533602715, -1], [5.52539205551, -1], [5.5254471302, -1], [5.52551913261, -1], [5.52561807632, -1], [5.52578115463, -1], [5.52584505081, -1], [5.52948713303, 1], [5.52967405319, 1], [5.53552317619, 1], [5.53568506241, 1], [5.59993219376, -1], [5.60015416145, -1], [5.60634708405, -1], [5.60645103455, -1], [5.6064851284, -1], [5.60650706291, -1], [5.60654306412, -1], [5.60660219193, -1], [5.6075091362, -1], [5.60753512383, -1], [5.60755610466, -1], [5.60757613182, -1], [5.60759615898, -1], [5.60761618614, -1], [5.60764908791, -1], [5.61388921738, -1], [5.6139690876, -1], [5.61401200294, -1], [5.61405110359, -1], [5.61408901215, -1], [5.61412405968, 1], [5.61417508125, -1], [5.61421322823, -1], [5.61428904533, -1], [5.66361999512, -1], [5.66378903389, -1], [5.84208607674, -1], [5.8423781395, -1], [5.98116016388, -1], [5.9812951088, -1], [5.99528717995, -1], [5.99546003342, -1], [5.99837708473, -1], [5.99847221375, -1], [5.99853110313, -1], [5.99858808517, -1], [5.99864315987, -1], [5.99869918823, -1], [5.99882411957, -1], [5.9990940094, -1], [5.99917912483, -1], [5.99923706055, -1], [5.99929213524, -1], [5.99934720993, -1], [5.99940299988, -1], [5.99945807457, -1], [6.020414114, -1], [6.02067422867, -1], [6.02087807655, -1], [6.02102708817, -1], [6.02109122276, -1], [6.02115011215, -1], [6.02124214172, -1], [6.12667417526, -1], [6.12680602074, 1], [6.12696814537, -1], [6.12723517418, -1], [6.13405108452, -1], [6.13410806656, -1], [6.79523420334, -1], [6.81173014641, -1], [6.8119699955, -1], [6.81215620041, -1], [6.81540322304, -1], [6.81549906731, -1], [6.81555604935, -1], [6.81561207771, -1], [6.8156671524, -1], [6.8157222271, -1], [6.81582021713, -1], [6.81595110893, -1], [6.81601119041, -1], [6.81606507301, -1], [6.81611919403, -1], [6.81617212296, -1], [6.81622600555, -1], [6.81628012657, -1], [6.81636714935, -1], [6.81747913361, -1], [6.8175880909, -1], [6.8176150322, -1], [6.81764221191, -1], [6.81766819954, -1], [6.8176920414, -1], [6.81771802902, -1], [6.81776118279, -1], [6.93424510956, -1], [6.93437218666, -1], [6.93445611, -1], [6.9344830513, -1], [6.93451714516, -1], [6.95054507256, -1], [6.95059609413, -1], [6.95061612129, -1], [6.95063614845, -1], [6.95065522194, -1], [6.95067501068, -1], [6.9507291317, -1], [6.95081710815, -1], [6.95084118843, -1], [6.95086121559, -1], [6.95088100433, -1], [6.95090103149, -1], [6.95092105865, -1], [6.95096302032, -1], [6.95099902153, -1], [6.95457911491, -1], [6.95471906662, -1], [6.9548201561, -1], [6.95487999916, -1], [6.95490908623, -1], [6.95495414734, -1], [6.95498108864, -1], [6.95504403114, -1], [6.95530319214, -1], [6.95537900925, -1], [6.95546913147, -1], [6.95552802086, -1], [6.95558309555, -1], [6.95564007759, -1], [6.95577001572, -1], [6.95592713356, -1], [6.95611310005, -1], [6.95622420311, -1], [6.95628619194, -1], [6.95634222031, -1], [6.9564011097, -1], [6.95646810532, -1], [6.95656013489, -1], [6.95673203468, -1], [6.9567990303, -1], [6.95685601234, -1], [6.95691609383, -1], [6.95697021484, -1], [6.95702409744, -1], [6.9570991993, -1], [6.95719218254, -1], [6.95736122131, -1], [6.95742702484, -1], [6.95748305321, -1], [6.9575381279, -1], [6.95758199692, 1], [6.95765399933, -1], [6.95771217346, -1], [6.95776605606, -1], [6.957873106, -1], [7.07325220108, -1], [7.073346138, -1], [7.07337617874, -1], [7.07340717316, -1], [7.07343316078, -1], [7.07345700264, -1], [7.07347917557, -1], [7.07351517677, -1], [7.07359814644, -1], [7.08937907219, -1], [7.08949708939, -1], [7.0895550251, -1], [7.08959913254, 1], [7.08967208862, -1], [7.08972811699, -1], [7.08978199959, -1], [7.08989715576, -1], [7.12293815613, 1], [7.4084610939, -1], [7.40878009796, -1], [7.41539001465, -1], [7.41549301147, -1], [7.41555118561, -1], [7.41560602188, -1], [7.4156601429, -1], [7.41571712494, -1], [7.41584300995, -1], [7.41912221909, -1], [7.41921901703, -1], [7.41927719116, -1], [7.4193341732, -1], [7.41938900948, -1], [7.41944408417, -1], [7.41949915886, -1], [7.41962218285, -1], [7.41977310181, -1], [7.41983509064, -1], [7.41990613937, -1], [7.41996407509, -1], [7.42001914978, -1], [7.42007708549, -1], [7.42013216019, -1], [7.42022109032, -1], [7.42033910751, -1], [7.420399189, -1], [7.42045402527, -1], [7.42050719261, -1], [7.42056012154, -1], [7.42061305046, -1], [7.42066001892, 1], [7.42073202133, -1], [7.42083501816, -1], [7.4209830761, -1], [7.42562699318, -1], [7.42572307587, -1], [7.42578101158, -1], [7.42583608627, -1], [7.42589211464, -1], [7.42594718933, -1], [7.4260661602, -1], [7.42619609833, -1], [7.42625713348, -1], [7.42631316185, -1], [7.42636799812, -1], [7.42642211914, -1], [7.42647600174, -1], [7.42653012276, -1], [7.42662000656, -1], [7.42667508125, -1], [7.42677211761, -1], [7.42933702469, -1], [7.42947220802, -1], [7.42953515053, -1], [7.42959213257, -1], [7.42964720726, -1], [7.42970204353, -1], [7.42975711823, -1], [7.42987918854, -1], [7.42998719215, -1], [7.4300801754, -1], [7.43019509315, -1], [7.43025708199, -1], [7.43031215668, -1], [7.43037319183, -1], [7.4304420948, -1], [7.43049907684, -1], [7.43059015274, -1], [7.43126106262, -1], [7.43138599396, -1], [7.43153119087, -1], [7.43159222603, -1], [7.43164801598, -1], [7.43170213699, -1], [7.43175601959, -1], [7.43180918694, -1], [7.43186306953, -1], [7.43225812912, -1], [7.43232011795, -1], [7.43237519264, -1], [7.43242907524, -1], [7.43247699738, 1], [7.43254899979, -1], [7.43260407448, -1], [7.43272399902, -1], [7.43285512924, -1], [7.43530201912, -1], [7.4354031086, -1], [7.43546104431, -1], [7.435516119, -1], [7.4355700016, -1], [7.43562507629, -1], [7.43571710587, -1], [7.43582320213, -1], [7.43887519836, -1], [7.4389591217, -1], [7.43897914886, -1], [7.43899512291, 1], [7.43902301788, -1], [7.43905806541, -1], [7.4390771389, -1], [7.43909716606, -1], [7.44028806686, -1], [7.44043803215, -1], [7.44051218033, -1], [7.44055509567, -1], [7.44057822227, -1], [7.44060707092, -1], [7.44062805176, -1], [7.44064807892, -1], [7.44069218636, -1], [7.44073104858, -1], [7.44235301018, -1], [7.44244599342, -1], [7.44246816635, -1], [7.44248914719, -1], [7.44251203537, -1], [7.44253206253, -1], [7.44255208969, -1], [7.44258713722, -1], [7.4431951046, -1], [7.44321918488, -1], [7.44323801994, -1], [7.44325613976, -1], [7.44327402115, -1], [7.44329214096, -1], [7.44331002235, -1], [7.4433400631, -1], [7.44462919235, -1], [7.44471406937, -1], [7.44473314285, -1], [7.44475221634, -1], [7.44477009773, -1], [7.44478702545, 1], [7.44481015205, -1], [7.44482922554, -1], [7.54791903496, -1], [7.5481262207, -1], [7.5483109951, -1], [7.54838013649, -1], [7.56926703453, 1], [7.57782101631, 1], [7.58805012703, 1], [7.58823013306, 1], [7.58856701851, 1], [7.5886900425, 1], [7.76260304451, -1], [7.76402521133, -1], [7.76476407051, -1], [7.76479315758, -1], [7.76482701302, -1], [7.76485013962, -1], [7.7648730278, -1], [7.76489806175, -1], [7.76493406296, -1], [7.76551604271, -1], [7.7655441761, -1], [7.76556801796, -1], [7.76559019089, -1], [7.76561307907, -1], [7.76564407349, -1], [7.76566720009, -1], [7.76570415497, -1], [7.77462005615, -1], [7.77466917038, -1], [7.7746860981, 1], [7.77471613884, -1], [7.77473521233, -1], [7.77475404739, -1], [7.77477312088, -1], [7.77481603622, -1], [7.77490210533, -1], [7.77659416199, -1], [7.77667808533, -1], [7.77672815323, -1], [7.77677416801, -1], [7.7768201828, -1], [7.77686405182, -1], [7.77694010735, -1], [7.78296899796, 1], [7.78311300278, 1], [7.78317403793, 1], [7.80381822586, -1], [7.80389618874, -1], [7.80392503738, -1], [7.80395007133, -1], [7.80397701263, -1], [7.8040201664, -1], [7.8077480793, -1], [7.80779600143, -1], [7.82003903389, -1], [7.82009220123, -1], [7.82011818886, -1], [7.82014322281, -1], [7.82017016411, -1], [7.82020521164, -1], [7.82025003433, -1], [7.9027261734, -1], [7.90281605721, -1], [7.90285110474, -1], [7.90288209915, -1], [7.90290808678, -1], [7.93834710121, -1], [7.93847703934, -1], [7.93855905533, -1], [7.94498300552, -1], [7.94504404068, -1], [7.94506907463, -1], [7.94510102272, -1], [7.94514417648, -1], [7.94516801834, -1], [7.94518613815, 1], [7.94524717331, -1], [8.07693314552, -1], [8.07702803612, -1], [8.07706713676, -1], [8.07709407806, -1]]


    def test_transmission_size_features(self):
        kNN.get_transmission_size_features(self.trace, self.features)

        self.assertEqual(len(self.features), 4)
        self.assertEqual(self.features[0], 436)
        self.assertEqual(self.features[1], 38)
        self.assertEqual(self.features[2], 398)
        self.assertEqual(self.features[3], 4.614383935919999)

    def test_packet_ordering(self):
        kNN.get_packet_ordering(self.trace, self.features)

        self.assertEqual(len(self.features), 600)
        self.assertEqual(self.features[300], 2)

    def test_concentration_packets(self):
        kNN.concentraction_packets(self.trace, self.features)

        self.assertEqual(len(self.features), 100)
        self.assertEqual(self.features[0], 4)

    def test_bursts(self):
        kNN.bursts(self.trace, self.features)

        self.assertEqual(len(self.features), 11)

    def test_first_20_packets(self):
        kNN.first_20_packets(self.trace, self.features)

        self.assertEqual(len(self.features), 20)

    def test_total(self):
        features = kNN.extract_kNN_features(self.trace)

        # Total amount of features
        self.assertEqual(len(features), 735)
