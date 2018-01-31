from __future__ import print_function, division, unicode_literals
import os
import unittest
try:
    import Image
except ImportError:
    from PIL import Image
from pytesseract import image_to_data, image_to_string, Output


class TestImageToX(unittest.TestCase):

    def setUp(self):
        self.tessdata_dir_config = '--tessdata-dir "/home/binhnq/VisualRecognition/tessdata"'
        self.img_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/test.png'
        self.img = Image.open(self.img_path)
        self.result_txt = """This is a lot of 12 point text to test the
ocr code and see if it works on all types
of file format.

The quick brown dog jumped over the
lazy fox. The quick brown dog jumped
over the lazy fox. The quick brown dog
jumped over the lazy fox. The quick
brown dog jumped over the lazy fox."""

        self.result_tsv = """level	page_num	block_num	par_num	line_num	word_num	left	top	width	height	conf	text
1	1	0	0	0	0	0	0	640	480	-1	
2	1	1	0	0	0	36	92	582	269	-1	
3	1	1	1	0	0	36	92	582	92	-1	
4	1	1	1	1	0	36	92	544	30	-1	
5	1	1	1	1	1	36	92	60	24	89	This
5	1	1	1	1	2	109	92	20	24	89	is
5	1	1	1	1	3	141	98	15	18	99	a
5	1	1	1	1	4	169	92	32	24	93	lot
5	1	1	1	1	5	212	92	28	24	91	of
5	1	1	1	1	6	251	92	31	24	91	12
5	1	1	1	1	7	296	92	68	30	92	point
5	1	1	1	1	8	374	93	53	23	85	text
5	1	1	1	1	9	437	93	26	23	93	to
5	1	1	1	1	10	474	93	52	23	90	test
5	1	1	1	1	11	536	92	44	24	87	the
4	1	1	1	2	0	36	126	582	31	-1	
5	1	1	1	2	1	36	132	45	18	93	ocr
5	1	1	1	2	2	91	126	69	24	91	code
5	1	1	1	2	3	172	126	51	24	94	and
5	1	1	1	2	4	236	132	50	18	88	see
5	1	1	1	2	5	299	126	15	24	96	if
5	1	1	1	2	6	325	126	14	24	88	it
5	1	1	1	2	7	348	126	85	24	90	works
5	1	1	1	2	8	445	132	33	18	94	on
5	1	1	1	2	9	500	126	29	24	91	all
5	1	1	1	2	10	541	127	77	30	89	types
4	1	1	1	3	0	36	160	187	24	-1	
5	1	1	1	3	1	36	160	28	24	91	of
5	1	1	1	3	2	72	160	41	24	92	file
5	1	1	1	3	3	123	160	100	24	88	format.
3	1	1	2	0	0	36	194	561	167	-1	
4	1	1	2	1	0	36	194	549	31	-1	
5	1	1	2	1	1	36	194	55	24	94	The
5	1	1	2	1	2	102	194	75	30	90	quick
5	1	1	2	1	3	189	194	85	24	91	brown
5	1	1	2	1	4	287	194	52	31	90	dog
5	1	1	2	1	5	348	194	108	31	91	jumped
5	1	1	2	1	6	468	200	63	18	94	over
5	1	1	2	1	7	540	194	45	24	87	the
4	1	1	2	2	0	37	228	548	31	-1	
5	1	1	2	2	1	37	228	55	31	89	lazy
5	1	1	2	2	2	103	228	50	24	91	fox.
5	1	1	2	2	3	165	228	55	24	98	The
5	1	1	2	2	4	232	228	75	30	91	quick
5	1	1	2	2	5	319	228	85	24	93	brown
5	1	1	2	2	6	417	228	51	31	93	dog
5	1	1	2	2	7	478	228	107	31	92	jumped
4	1	1	2	3	0	36	262	561	31	-1	
5	1	1	2	3	1	36	268	63	18	93	over
5	1	1	2	3	2	109	262	44	24	90	the
5	1	1	2	3	3	165	262	56	31	91	lazy
5	1	1	2	3	4	231	262	50	24	93	fox.
5	1	1	2	3	5	294	262	55	24	95	The
5	1	1	2	3	6	360	262	75	30	90	quick
5	1	1	2	3	7	447	262	85	24	91	brown
5	1	1	2	3	8	545	262	52	31	90	dog
4	1	1	2	4	0	43	296	518	31	-1	
5	1	1	2	4	1	43	296	107	31	91	jumped
5	1	1	2	4	2	162	302	64	18	91	over
5	1	1	2	4	3	235	296	44	24	94	the
5	1	1	2	4	4	292	296	55	31	92	lazy
5	1	1	2	4	5	357	296	50	24	91	fox.
5	1	1	2	4	6	420	296	55	24	94	The
5	1	1	2	4	7	486	296	75	30	91	quick
4	1	1	2	5	0	37	330	524	31	-1	
5	1	1	2	5	1	37	330	85	24	91	brown
5	1	1	2	5	2	135	330	52	31	90	dog
5	1	1	2	5	3	196	330	108	31	91	jumped
5	1	1	2	5	4	316	336	63	18	94	over
5	1	1	2	5	5	388	330	45	24	94	the
5	1	1	2	5	6	445	330	55	31	96	lazy
5	1	1	2	5	7	511	330	50	24	91	fox."""

    def test_image_to_string(self):
        text = image_to_string(self.img, config=self.tessdata_dir_config)
        self.assertEqual(self.result_txt, text)

    def test_image_to_data(self):
        out = image_to_data(self.img, config=self.tessdata_dir_config)
        self.assertEqual(self.result_tsv, out)

        out = image_to_data(self.img, config=self.tessdata_dir_config, output_type=Output.DICT)
        print(out)
