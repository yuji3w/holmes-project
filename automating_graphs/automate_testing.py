import subprocess


def make_pal_arg(minpallen, maxpallen, gaplimit, nummismatches):
	return """palindrome -sequence sequence.fasta -minpallen {} -maxpallen {} -gaplimit {} -nummismatches {} -outfile nc_000913.pal -nooverlap""".format(minpallen, maxpallen, gaplimit, nummismatches)

run_other_py_file = "python automate_parameters.py"

minpallen = 10
maxpallen = 100
for gaplimit in range(0, 50, 10):
	for nummismatches in range(0, 3):
		pal_arg = make_pal_arg(minpallen, maxpallen, gaplimit, nummismatches)
		subprocess.run([pal_arg], shell = True)
		subprocess.run([run_other_py_file], shell = True)