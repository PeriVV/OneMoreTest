# Table of Contents
- [Introduction](#introduction) 
- [Structure](#structure)
- [SourceCode Description](#sourcecode-description-code)
- [Operating Instruction](#operating-instruction)
    - [Test case generation](#test-case-generation)
    - [Environmental requirements](#environmental-requirements)
    - [OneMoreTest](#deeporacle)
    - [Random-based selection](#random-based-selection)
    - [Coverage-based selection](#coverage-based-selection)
    - [Daikon-based selection](#daikon-based-selection)
- [Table](#Table)
# Introduction
This is the replication package of the paper "One More Test: A Novel Approach to Generating and Selecting Fault-Revealing Unit Tests". It is composed of tools (including the proposed approach and baseline approaches) and data employed in the evaluation.

# Structure
- Code: source code of the experiment
- Data: TrainingData & TestingData of experiment
- Data/OneMoreTest: The experimental data of OneMoreTest
- Data/Random: The experimental data of random-based selection
- Data/Coverage: The experimental data of coverage-based selection
- Data/Daikon: The experimental data of daikon-based selection
- Gif: Instructions for generating test cases

# SourceCode Description (/Code)
- train.py: code file for training the neural network
- test.py: code file for testing the neural network & Test case prioritization
- loadData.py: Loading and processing data
- defines.py: code file for defining the file path
- Coverage.py: main file for coverage-based selection
- daikon.py: main file for daikon-based selection
- DataGenerator.jar: Jar package for random generation of test cases
- GenerateTestCases: IDEA plug-in project that randomly generates test cases

# Operating Instruction
## Test case generation
- Download DataGenerator.jar,TestOracle project
- Run GenerateTestCases as IDEA plug-in project
- Import the DataGenerator.jar into the project under test
- Select the method under test(MUT)
- Click the ***Extract Variables*** button
- Click the ***Generate Data*** button
- Select the inputs and outputs to generate
- Click the ***Confirm*** button
- Manually set ranges for inputs based on data type
- Click the ***Generate*** button
- Then you will see the ***before_data.txt*** and ***after_data.txt*** under the project folder

![image](https://github.com/OneMoreTest/OneMoreTest/blob/main/Gif/generateString.gif)
![image](https://github.com/OneMoreTest/OneMoreTest/blob/main/Gif/generateDouble.gif)

## Environmental requirements
- jdk1.8/jdk11
- python3.6
- daikon

- Daikon (only for daikon-based selection)
    - Download daikon from [Daikon](http://plse.cs.washington.edu/daikon/download/)
    - Install Daikon environment according to the [Daikon Documentation](http://plse.cs.washington.edu/daikon/download/doc/daikon.html#Installing-Daikon)
    - Compile the target java files: run ```javac -g RootPath/*.java```
    - Run DynComp: ```java -cp .:$DAIKONDIR/daikon.jar daikon.Chicory --daikon --comparability-file=ClassName.decls-DynComp PackageName.ClassName```
    - Run Chicory: ```java -cp .:$DAIKONDIR/daikon.jar daikon.Chicory --comparability-file=ClassName.decls-DynComp PackageName.ClassName```
    - Run Daikon: ```java -cp $DAIKONDIR/daikon.jar daikon.Daikon ClassName.dtrace.gz > daikon.txt```

## OneMoreTest
- Generate Test cases
    - before_data.txt: the input of test cases
    - after_data.txt: the output of test cases
    - label.txt: the label of test cases (only for testing)
<img src='./Fig/Data.jpg' align=center />

- Select the corresponding data processing function: ``` loadData.load_isInner_before(before_file)```
<img src='./Fig/LoadData.png' align=center />

- Run ```python main.py```

## Random-based selection
- Load the corresponding data as dataset.(input,output,label)
<img src='./Fig/RandomTest.jpg' align=center />

- execute ```random.shuffle(dataset)```
<img src='./Fig/Random.jpg' align=center />

- Run ```python count_label.py```

## Coverage-based selection
- Select the corresponding test case and line coverage file path (```load_file(compare_path)```)
<img src='./Fig/Coverage.jpg' align=center />

- Run ```python Coverage.py```

## Daikon-based selection
- Run Daikon on MUT and get Daikon output information
<img src='./Fig/DaikonInfo.jpg' align=center />

- Generate the sorting algorithm base on the output of daikon
<img src='./Fig/Algorithm.png' align=center />

- Select the corresponding sorting algorithm of MUT: ```main(method_path, 71)```
<img src='./Fig/Daikon.jpg' align=center />

- Run ```python daikon.py```

#Table
|  表头   | 表头  |
|  ----  | ----  |
| 单元格  | 单元格 |
| 单元格  | 单元格 |


