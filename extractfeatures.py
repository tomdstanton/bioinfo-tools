# Usage:
# python extractfeatures.py infile.gbk outfile.faa

from Bio import SeqIO
import sys

with open(sys.argv[2], 'w') as ofh:
        for seq_record in SeqIO.parse(sys.argv[1], 'genbank'):
                for seq_feature in seq_record.features:
                        if seq_feature.type=="CDS":
                                assert len(seq_feature.qualifiers['translation'])==1
                                try:
					name = seq_feature.qualifiers['gene'][0]
				except KeyError:
					name = seq_feature.qualifiers['product'][0]
                                ofh.write(">%s\n%s\n" % (
				name,
                                seq_feature.qualifiers['translation'][0]))
