# Components of State Machine
## Transitions
+ Takes in base pair and outputs
    + None, advances to next input, or
    + Advances to next state machine, perhaps without an input
+ Takes in base pair and outputs
    + Own base pair, advances to next input, or
    + Advances to next state machine, perhaps without an input
+ Takes in base pair and outputs
    + None, advances to next input, or
    + Advances to next state machine, perhaps without an input
+ Ends input or inputs None for all inputs

Align this sequence with desired output TTTT

## Weights
+ Every weight will be 1
+ Where is this seen in the JSON?

## Code attempt
`test_alignment.json`:
```
{"state":
 [{"n":0,
   "id":["concat-l",["concat-l",["A","C","G","T"]]],
   "trans":[{"to":0,"in":"A"},
            {"to":0,"in":"C"},
            {"to":0,"in":"G"},
            {"to":0,"in":"T"},
            {"to":1}]},
  {"n":1,
   "id":["concat-l",["concat-r",["A","C","T","G"]]],
   "trans":[{"to":1,"in":"A","out":"A"},
            {"to":1,"in":"C","out":"C"},
            {"to":1,"in":"T","out":"T"},
            {"to":1,"in":"G","out":"G"},
            {"to":2}]},
  {"n":2,
   "id":["concat-r",["A","C","G","T"]],
   "trans":[{"to":2,"in":"A"},
            {"to":2,"in":"C"},
            {"to":2,"in":"G"},
            {"to":2,"in":"T"}]}
 ]
}

```
+ [SM n2 is unnecessary (left in because I don't know what the labels mean)]

Command:
```
boss test_alignment.json --input-fasta sequence.fasta --output-chars TTTT --counts
```

+ Why does thie not work?

Command:
```
boss --counts -v6 \
 --generate-uniform-dna \
 --concat \
  --begin \
   test_alignment.json \
   --concat --generate-uniform-dna \
   --count-copies n \
  --end \
 --input-fasta test.fasta
```

+ I don't understand how the syntax works & am getting:
```
Command '--begin' ==> left bracket '('
Command '--count-copies' ==> Kleene star with dummy counting parameter
Advance-sorting 6 states: started at Fri Nov  8 12:59:01 2019
Sorting left machine unchanged with 1 backward silent transitions
Trying to sort again with "dummy" null start & end states...
Advance-sorting 8 states: started at Fri Nov  8 12:59:01 2019
Sorting left number of backward silent transitions unchanged at 1; restoring original order
Padding with "dummy" null states failed
Read 1 sequence from test.fasta
Abort: Assertion Failed: Machine is not topologically sorted
Stack trace:
boss() [0x46a39b]
boss() [0x46a1a9]
boss() [0x417695]
/lib/x86_64-linux-gnu/libc.so.6(__libc_start_main+0xe7) [0x7f5da0170b97]
boss() [0x40b5ea]
Abort

```