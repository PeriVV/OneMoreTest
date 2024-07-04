## Selected Projects From Defects4J -- version 1.0.0

| Identifier | Project name        | Number of bugs | #Bugs selected for evaluation |
| ---------- | ------------------- | -------------- | ---------------------------- |
| Chart      | JFreechart          | 26             | 15                           |
| Closure    | Closure compiler    | 133            | 49                           |
| Lang       | Apache commons-lang | 63             | 44                           |
| Math       | Apache commons-math | 106            | 48                           |
| Time       | Joda-Time           | 27             | 22                           |
| **Total**  |                     | **355**        | **178**                      |

## Selected Real-world Faulty Methods

|  ID  |         BugID          |                                                                       Method Signature                                                                       | Size(LOC) | # Invoked Methods |
| :--: | :--------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: | :-------: | :---------------: |
|  M1  |        Chart_3         |                                            TimeSeries createCopy(RegularTimePeriod start, RegularTimePeriod end)                                             |    38     |         9         |
|  M2  |        Chart_5         |                                                          XYDataItem addOrUpdate(Number x, Number y)                                                          |    37     |         9         |
|  M3  |        Chart_7         |                                                       void updateBounds(TimePeriod period, int index)                                                        |    78     |        32         |
|  M4  |        Chart_9         |                                            TimeSeries createCopy(RegularTimePeriod start, RegularTimePeriod end)                                             |    38     |         9         |
|  M5  |        Chart_13        |                               Size2D arrangeFF(BlockContainer container, Graphics2D g2, <br/> RectangleConstraint constraint)                                |    67     |        22         |
|  M6  |        Chart_16        |                  DefaultIntervalCategoryDataset(Comparable[] seriesKeys, <br/> Comparable[] categoryKeys,Number[][] starts,Number[][] ends)                  |    70     |         8         |
|  M7  |        Chart_18        |                                                           void removeColumn(Comparable columnKey)                                                            |     7     |         5         |
|  M8  |        Chart_20        |                      ValueMarker(double value, Paint paint, Stroke stroke, <br/>Paint outlinePaint, Stroke outlineStroke, float alpha)                       |     4     |         1         |
|  M9  |        Chart_21        |                                                            DefaultBoxAndWhiskerCategoryDataset()                                                             |     9     |         2         |
| M10  |        Chart_22        |                                                  void removeObject(Comparable rowKey, Comparable columnKey)                                                  |    24     |         5         |
| M11  |        Chart_24        |                                                                  boolean equals(Object obj)                                                                  |    19     |         2         |
| M12  |    Time_3_addYears     |                                                                      void addYears(int)                                                                      |     3     |         5         |
| M13  |    Time_3_addMonths    |                                                                     void addMonths(int)                                                                      |     3     |         5         |
| M14  |    Time_3_addWeeks     |                                                                      void addWeeks(int)                                                                      |     3     |         5         |
| M15  |     Time_3_addDays     |                                                                      void addDays(int)                                                                       |     3     |         5         |
| M16  |         Time_4         |                                                     Partial with(DateTimeFieldType fieldType, int value)                                                     |    48     |        24         |
| M17  |         Time_6         |                          GJChronology getInstance(DateTimeZone zone, <br/> ReadableInstant gregorianCutover,int minDaysInFirstWeek)                          |    45     |        13         |
| M18  |    Time_7_parseInto    |                                          int parseInto(ReadWritableInstant instant, <br/>String text, int position)                                          |    28     |        19         |
| M19  | Time_7_mutableDateTime |                                                      MutableDateTime parseMutableDateTime(String text)                                                       |    26     |        16         |
| M20  |         Time_8         |                                            DateTimeZone forOffsetHoursMinutes(int hoursOffset, int minutesOffset)                                            |    23     |         5         |
| M21  |        Time_10         |                                  int between(ReadablePartial start, ReadablePartial end, <br/>ReadablePeriod zeroInstance)                                   |    18     |        16         |
| M22  |        Time_12         |                                                           LocalDateTime fromDateFields(Date date)                                                            |    14     |         9         |
| M23  |  Time_14_minusMonths   |                                                                  MonthDay minusMonths(int)                                                                   |     3     |         3         |
| M24  |   Time_14_plusMonths   |                                                                   MonthDay plusMonths(int)                                                                   |     3     |         2         |
| M25  |        Time_15         |                                                            long safeMultiply(long val1, int val2)                                                            |    15     |         1         |
| M26  |        Time_17         |                                                   long adjustOffset(long instant, boolean earlierOrLater)                                                    |    17     |         4         |
| M27  |        Time_18         |                                      long getDateTimeMillis(int year, int monthOfYear, int dayOfMonth, int millisOfDay)                                      |    22     |         4         |
| M28  |        Time_22         |                                                               Period parsePeriod(String text)                                                                |     4     |         3         |
| M29  |        Time_24         |                                                     long computeMillis(boolean resetFields, String text)                                                     |    47     |        12         |
| M30  |        Time_26         |                                                              long add(long instant, int value)                                                               |    10     |         5         |
| M31  |        Time_27         |                              PeriodFormatter toFormatter(List<Object> elementPairs, <br/>boolean notPrinter, boolean notParser)                              |    19     |        13         |
| M32  |         Lang_1         |                                                               Number createNumber(String str)                                                                |    158    |        55         |
| M33  |         Lang_6         |                                                          translate(CharSequence input, Writer out)                                                           |    23     |         6         |
| M34  |         Lang_7         |                                                               Number createNumber(String str)                                                                |    153    |        53         |
| M35  |         Lang_8         |                                                    void appendTo(StringBuffer buffer, Calendar calendar)                                                     |     7     |         6         |
| M36  |         Lang_9         |                                                                         void init()                                                                          |    36     |        21         |
| M38  |        Lang_12         |                       String random(int count, int start, int end, boolean letters, <br/>boolean numbers, char[] chars, Random random)                       |    60     |         8         |
| M39  |        Lang_17         |                                                        void translate(CharSequence input, Writer out)                                                        |    29     |         6         |
| M40  |        Lang_19         |                                                   int translate(CharSequence input, int index, Writer out)                                                   |    44     |        14         |
| M41  |        Lang_21         |                                                    boolean isSameLocalTime(Calendar cal1, Calendar cal2)                                                     |    12     |        17         |
| M42  |        Lang_22         |                                                           int greatestCommonDivisor(int u, int v)                                                            |    44     |         3         |
| M43  |        Lang_26         |                                                                   String format(Date date)                                                                   |     4     |         5         |
| M44  |        Lang_27         |                                                               Number createNumber(String str)                                                                |    150    |        47         |
| M45  |        Lang_28         |                                                   int translate(CharSequence input, int index, Writer out)                                                   |    32     |        11         |
| M46  |        Lang_36         |                                                                 boolean isNumber(String str)                                                                 |    94     |         2         |
| M47  |        Lang_38         |                                                   StringBuffer format(Calendar calendar, StringBuffer buf)                                                   |     6     |         3         |
| M48  |        Lang_39         |                     String replaceEach(String text, String[] searchList, <br/>String[] replacementList, boolean repeat, int timeToLive)                      |    126    |        13         |
| M49  |        Lang_41         |                                                          String getShortClassName(String className)                                                          |    19     |         4         |
| M50  |        Lang_43         |                      StringBuffer appendQuotedString(String pattern, ParsePosition pos, <br/>StringBuffer appendTo, boolean escapingOn)                      |    28     |        15         |
| M51  |        Lang_44         |                                                               Number createNumber(String val)                                                                |    148    |        48         |
| M52  |        Lang_45         |                                           String abbreviate(String str, int lower, int upper, String appendToEnd)                                            |    38     |        17         |
| M53  |        Lang_46         |                                                                String escapeJava(String str)                                                                 |     3     |         1         |
| M54  |        Lang_48         |                                                         EqualsBuilder append(Object lhs, Object rhs)                                                         |    42     |        14         |
| M55  |        Lang_49         |                                                                      Fraction reduce()                                                                       |     9     |         3         |
| M56  |        Lang_53         |                                                     void modify(Calendar val, int field, boolean round)                                                      |    126    |        18         |
| M57  |        Lang_54         |                                                                 Locale toLocale(String str)                                                                  |    36     |        18         |
| M58  |        Lang_57         |                                                           boolean isAvailableLocale(Locale locale)                                                           |     2     |         2         |
| M59  |        Lang_58         |                                                               Number createNumber(String str)                                                                |    147    |        48         |
| M60  |        Lang_59         |                                           StrBuilder appendFixedWidthPadRight(Object obj, int width, char padChar)                                           |    17     |         6         |
| M61  |        Lang_61         |                                                           int indexOf(String str, int startIndex)                                                            |    27     |         3         |
| M62  |        Lang_64         |                                                         int getValueInOtherClassLoader(Object other)                                                         |    13     |         5         |
| M63  |        Lang_65         |                                                     void modify(Calendar val, int field, boolean round)                                                      |    77     |        13         |
| M64  |       Math_4j_1        |                           BigFraction(final double value, final double epsilon, <br/>final int maxDenominator, int maxIterations)                            |    66     |         9         |
| M65  |       Math_4j_2        |                                                                      getNumericalMean()                                                                      |     3     |         3         |
| M66  |       Math_4j_9        |                                                                        Line revert()                                                                         |     3     |         1         |
| M67  |       Math_4j_10       |           void atan2(final double[] y, final int yOffset, final double[] x, <br/>final int xOffset, final double[] result, final int resultOffset)           |    38     |        12         |
| M68  |       Math_4j_11       |                                                             double density(final double[] vals)                                                              |     9     |         5         |
| M69  |       Math_4j_16       |                                                                    double cosh(double x)                                                                     |    54     |         3         |
| M70  |       Math_4j_17       |                                                                  Dfp multiply(final int x)                                                                   |     3     |         1         |
| M71  |       Math_4j_21       |                                              RectangularCholeskyDecomposition(RealMatrix matrix, double small)                                               |    89     |         7         |
| M72  |       Math_4j_26       |                                        Fraction(double value, double epsilon, int maxDenominator, int maxIterations)                                         |    63     |         7         |
| M73  |       Math_4j_27       |                                                                   double percentageValue()                                                                   |     3     |         2         |
| M74  |       Math_4j_30       |                                       double calculateAsymptoticPValue(final double Umin, final int n1, final int n2)                                        |    16     |         3         |
| M75  |       Math_4j_31       |                                                       int inverseCumulativeProbability(final double p)                                                       |    43     |        14         |
| M76  |       Math_4j_33       |                                                                  void dropPhase1Objective()                                                                  |    40     |        14         |
| M77  |       Math_4j_34       |                                                               Iterator<Chromosome> iterator()                                                                |     3     |         1         |
| M78  |       Math_4j_41       |                  double evaluate(final double[] values, final double[] weights, <br/>final double mean, final int begin, final int length)                   |    31     |         1         |
| M79  |       Math_4j_42       |                                                               RealPointValuePair getSolution()                                                               |    29     |        12         |
| M80  |       Math_4j_48       |                                                                    final double doSolve()                                                                    |    122    |        14         |
| M81  |       Math_4j_49       |                                                          OpenMapRealVector ebeDivide(RealVector v)                                                           |     9     |         8         |
| M82  |       Math_4j_53       |                                                                   Complex add(Complex rhs)                                                                   |     5     |         4         |
| M83  |       Math_4j_58       |                                                                        double[] fit()                                                                        |     4     |         4         |
| M84  |       Math_4j_59       |                                                           float max(final float a, final float b)                                                            |     3     |         1         |
| M85  |       Math_4j_62       |          UnivariateRealPointValuePair optimize(final FUNC f, final GoalType goal, <br/>final double min, final double max, final double startValue)          |    33     |         8         |
| M86  |       Math_4j_63       |                                                              boolean equals(double x, double y)                                                              |     3     |         2         |
| M87  |       Math_4j_65       |                                                                       double getRMS()                                                                        |     7     |         0         |
| M88  |       Math_4j_74       |         double integrate(final FirstOrderDifferentialEquations equations, <br/>final double t0, final double[] y0, final double t, final double[] y)         |    167    |        36         |
| M89  |       Math_4j_75       |                                                                double getPct(Comparable<?> v)                                                                |     6     |         2         |
| M90  |       Math_4j_80       |                                                     boolean flipIfWarranted(final int n, final int step)                                                     |    15     |         0         |
| M91  |       Math_4j_81       |                                                            void processGeneralBlock(final int n)                                                             |    106    |         8         |
| M92  |       Math_4j_90       |                                                                   void addValue(Object v)                                                                    |    27     |         9         |
| M93  |       Math_4j_91       |                                                                int compareTo(Fraction object)                                                                |     4     |         2         |
| M94  |       Math_4j_94       |                                                                    int gcd(int u, int v)                                                                     |    49     |         3         |
| M95  |       Math_4j_95       |                                                 void setDenominatorDegreesOfFreedom(double degreesOfFreedom)                                                 |     6     |         1         |
| M96  |       Math_4j_96       |                                                                 boolean equals(Object other)                                                                 |    22     |         7         |
| M97  |       Math_4j_97       |                                                             double solve(double min, double max)                                                             |    27     |         6         |
| M98  |       Math_4j_98       |                                                             BigDecimal[] operate(BigDecimal[] v)                                                             |    15     |         3         |
| M99  |      Math_4j_105       |                                                                 double getSumSquaredErrors()                                                                 |     3     |         0         |
| M100 |      Math_4j_106       |                                                       Fraction parse(String source, ParsePosition pos)                                                       |    76     |        26         |
| M101 |       Closure_3        |                                                      void removeUnreferencedFunctionArgs(Scope fnScope)                                                      |    29     |         9         |
| M102 |       Closure_20       |                                                            Node tryFoldSimpleFunctionCall(Node n)                                                            |    22     |        14         |
| M103 |       Closure_23       |                                                    Node tryFoldArrayAccess(Node n, Node left, Node right)                                                    |    50     |        11         |
| M104 |       Closure_26       |                                         void emitOptionalModuleExportsOverride<br/>(Node script, String moduleName)                                          |    10     |        10         |
| M105 |       Closure_27       |                                                       Node tryFinally(Node tryBody, Node finallyBody)                                                        |     5     |         6         |
| M106 |       Closure_37       |                                                          void traverseFunction(Node n, Node parent)                                                          |    35     |        13         |
| M107 |       Closure_40       |                                                       void visit(NodeTraversal t, Node n, Node parent)                                                       |    42     |        22         |
| M108 |       Closure_41       |                      FunctionTypeBuilder inferFromOverriddenFunction <br/>(@Nullable FunctionType oldType, @Nullable Node paramsParent)                      |    54     |        21         |
| M109 |       Closure_44       |                                                                   void add(String newcode)                                                                   |    21     |         5         |
| M110 |       Closure_57       |                                       String extractClassNameIfGoog(Node node, <br/>Node parent, String functionName)                                        |    16     |         7         |
| M111 |       Closure_58       |                                             computeGenKill(Node n, BitSet gen, BitSet kill, boolean conditional)                                             |    85     |        35         |
| M112 |       Closure_67       |                                                        boolean isPrototypePropertyAssign(Node assign)                                                        |    20     |        11         |
| M113 |       Closure_68       |                                                       Node parseBasicTypeExpression(JsDocToken token)                                                        |    25     |        19         |
| M114 |       Closure_71       |                                           void checkPropertyVisibility(NodeTraversal t, Node getprop, Node parent)                                           |    93     |        26         |
| M115 |       Closure_85       |                                                         Node tryRemoveUnconditionalBranching(Node n)                                                         |    62     |        22         |
| M116 |       Closure_88       |                                              VariableLiveness isVariableReadBeforeKill(Node n, String variable)                                              |    11     |         4         |
| M117 |       Closure_91       |                                                 boolean shouldTraverse(NodeTraversal t, Node n, Node parent)                                                 |    64     |        20         |
| M118 |      Closure_105       |                                   void tryFoldStringJoin(NodeTraversal t, Node n, <br/>Node left, Node right, Node parent)                                   |    88     |        14         |
| M119 |      Closure_108       |                                                               void exitScope(NodeTraversal t)                                                                |    13     |         5         |
| M120 |      Closure_109       |                                                      Node parseContextTypeExpression(JsDocToken token)                                                       |     3     |         1         |
| M121 |      Closure_112       |                                             boolean inferTemplatedTypesForCall(<br/>Node n, FunctionType fnType)                                             |    27     |        11         |
| M122 |      Closure_114       |                                               void recordAssignment(NodeTraversal t, Node n, Node recordNode)                                                |    30     |         9         |
| M123 |      Closure_116       |                                                      Node inlineReturnValue(Node callNode, Node fnNode)                                                      |    31     |        15         |
| M124 |      Closure_117       |                                                  String getReadableJSTypeName(Node n, boolean dereference)                                                   |    53     |        24         |
| M125 |      Closure_125       |                                                            void visitNew(NodeTraversal t, Node n)                                                            |    15     |        11         |
| M126 |      Closure_126       |                                                void tryMinimizeExits(Node n, int exitType, String labelName)                                                 |    95     |        33         |
| M127 |        Lang_52         |                                        void escapeJavaStyleString(Writer out, String str, boolean escapeSingleQuote)                                         |    75     |        25         |
| M128 |        Chart_2         |                                            Range iterateDomainBounds(XYDataset dataset, boolean includeInterval)                                             |    45     |        13         |
| M129 |       Math_4j_88       |                                                               RealPointValuePair getSolution()                                                               |    21     |         9         |
| M130 |      Closure_133       |                                                                String getRemainingJSDocLine()                                                                |     4     |         1         |
| M131 |       Closure_83       |                                                            int parseArguments(Parameters params)                                                             |    19     |         7         |
| M132 |         Time_9         |                                            DateTimeZone forOffsetHoursMinutes(int hoursOffset, int minutesOffset)                                            |    20     |         7         |
| M133 |        Time_13         |                                             void printTo(StringBuffer buf, ReadablePeriod period, Locale locale)                                             |    29     |         8         |
| M134 |        Lang_24         |                                                                 boolean isNumber(String str)                                                                 |    102    |         2         |
| M135 |       Closure_28       |                                                          static Class<?>[] toClass(Object[] array)                                                           |    11     |         0         |
| M136 |        Chart_10        |                                                      String generateToolTipFragment(String toolTipText)                                                      |     3     |         0         |
| M137 |        Lang_33         |                                                              Class<?>[] toClass(Object[] array)                                                              |    11     |         1         |
| M138 |       Math_4j_85       |              double[] bracket(UnivariateRealFunction function,double initial, <br/>double lowerBound, double upperBound, int maximumIterations)              |    43     |         4         |
| M139 |       Closure_62       |                                                        String format(JSError error, boolean warning)                                                         |    45     |        23         |
| M140 |      Closure_130       |                                                        void inlineAliases(GlobalNamespace namespace)                                                         |    36     |         9         |
| M141 |        Lang_60         |                                                                  boolean contains(char ch)                                                                   |     8     |         0         |
| M142 |        Lang_51         |                                                                boolean toBoolean(String str)                                                                 |    51     |        23         |
| M143 |        Lang_62         |                                                         void unescape(Writer writer, String string)                                                          |    66     |        21         |
| M144 |       Math_4j_22       |                                                            boolean isSupportUpperBoundInclusive()                                                            |     3     |         0         |
| M145 |        Lang_50         |                                         FastDateFormat getDateInstance(int style, TimeZone timeZone, Locale locale)                                          |    25     |        10         |
| M146 |        Chart_1         |                                                            LegendItemCollection getLegendItems()                                                             |    32     |        10         |
| M147 |       Closure_15       |                                                              boolean mayThrowException(Node n)                                                               |    20     |         5         |
| M148 |       Closure_35       |                                               void declareNameInScope(FlowScope scope, Node node, JSType type)                                               |    23     |        10         |
| M149 |      Closure_103       |                                                            boolean isFoldableExpressBlock(Node n)                                                            |    19     |         3         |
| M150 |       Closure_19       |                                                        String toStringHelper(boolean forAnnotations)                                                         |    43     |        14         |
| M151 |       Closure_87       |                                                               CompilerOptions createOptions()                                                                |    56     |        17         |
| M152 |       Closure_39       |                                                                String getLine(int lineNumber)                                                                |    41     |         5         |
| M153 |      Closure_107       |                                                         String normalizeSourceName(String filename)                                                          |    10     |         2         |
| M154 |       Closure_56       |                                                       boolean isInlinableObject(List<Reference> refs)                                                        |    85     |        17         |
| M155 |       Closure_9        |                                                                Node tryFoldArrayJoin(Node n)                                                                 |    109    |        47         |
| M156 |       Closure_29       | String strEscape(String s, char quote, String doublequoteEscape, <br/>String singlequoteEscape, String backslashEscape, CharsetEncoder outputCharsetEncoder) |    69     |        11         |
| M157 |       Closure_50       |                                                       Node tryFoldShift(Node n, Node left, Node right)                                                       |    61     |        12         |
| M158 |       Closure_77       |                                                        void handleObjectLit(NodeTraversal t, Node n)                                                         |    23     |        13         |
| M159 |       Closure_97       |                                                                        Complex atan()                                                                        |     7     |         7         |
| M160 |      Closure_118       |                               List<Cluster<T>> cluster(final Collection<T> points, <br/>final int k, final int maxIterations)                                |    25     |         7         |
| M161 |       Math_4j_47       |                                                               Complex divide(Complex divisor)                                                                |    29     |         8         |
| M162 |       Math_4j_79       |                                                             double distance(int[] p1, int[] p2)                                                              |     7     |         1         |
| M163 |        Lang_10         |                                        StringBuilder escapeRegex(StringBuilder regex, String value, boolean unquote)                                         |    40     |         6         |
| M164 |        Lang_16         |                                                               Number createNumber(String str)                                                                |    150    |        45         |
| M165 |        Lang_20         |                                        String join(Object[] array, char separator, <br/>int startIndex, int endIndex)                                        |    19     |         6         |
| M166 |        Lang_29         |                                                            float toJavaVersionInt(String version)                                                            |     3     |         2         |
| M167 |        Lang_55         |                                                                         void stop()                                                                          |     6     |         1         |
| M168 |       Math_4j_32       |                                                             void computeGeometricalProperties()                                                              |    51     |        16         |
| M169 |       Math_4j_43       |                                                                 void addValue(double value)                                                                  |    19     |         9         |
| M170 |      Closure_115       |                                            CanInlineResult canInlineReferenceDirectly(Node callNode, Node fnNode)                                            |    69     |        17         |
| M171 |        Chart_24        |                                                                 Paint getPaint(double value)                                                                 |     6     |         3         |
| M172 |        Lang_14         |                                                      boolean equals(CharSequence cs1, CharSequence cs2)                                                      |     9     |         1         |
| M173 |       Math_4j_15       |                                                                double pow(double x, double y)                                                                |    158    |         6         |
| M174 |       Math_4j_64       |                                                             VectorialPointValuePair doOptimize()                                                             |    223    |        20         |
| M175 |       Math_4j_66       |          double localMin(boolean isMinim, UnivariateRealFunction f, <br/>GoalType goalType, double lo, double mid, double hi, double eps, double t)          |    151    |         6         |
| M176 |       Math_4j_73       |                         double solve(final UnivariateRealFunction f, final double min, <br/>final double max, final double initial)                          |    42     |        13         |
| M177 |       Closure_17       |                              JSType getDeclaredType(String sourceName, JSDocInfo info, <br/>Node lValue, @Nullable Node rValue)                              |    50     |        25         |
| M178 |       Closure_65       | String strEscape(String s, char quote, String doublequoteEscape, <br/>String singlequoteEscape, String backslashEscape, CharsetEncoder outputCharsetEncoder) |    70     |        21         |

## Excluded Faulty methods

|  ID  | Excluded methods | Reason for Exclusion |
| :--: | :--------------: | :------------------: |
|  M1  |     Chart_4      |   100% error rate    |
|  M2  |     Chart_6      |   100% error rate    |
|  M3  |     Chart_8      |   100% error rate    |
|  M4  |     Chart_11     |   100% error rate    |
|  M5  |     Chart_12     |   100% error rate    |
|  M6  |     Chart_14     |   100% error rate    |
|  M7  |     Chart_15     |   100% error rate    |
|  M8  |     Chart_17     |   100% error rate    |
|  M9  |     Chart_19     |   100% error rate    |
| M10  |     Chart_23     |   100% error rate    |
| M11  |     Chart_25     |   100% error rate    |
| M12  |     Chart_26     |   100% error rate    |
| M13  |      Time_1      |   100% error rate    |
| M14  |      Time_2      |   100% error rate    |
| M15  |      Time_5      |   100% error rate    |
| M16  |     Time_11      |   100% error rate    |
| M17  |     Time_16      |   100% error rate    |
| M18  |     Time_19      |   100% error rate    |
| M19  |     Time_20      |   100% error rate    |
| M20  |     Time_23      |   100% error rate    |
| M21  |     Time_25      |   100% error rate    |
| M22  |      Lang_3      |   100% error rate    |
| M23  |      Lang_4      |   100% error rate    |
| M24  |      Lang_5      |   100% error rate    |
| M25  |     Lang_13      |   100% error rate    |
| M26  |     Lang_18      |   100% error rate    |
| M27  |     Lang_23      |   100% error rate    |
| M28  |     Lang_25      |   100% error rate    |
| M29  |     Lang_30      |   100% error rate    |
| M30  |     Lang_31      |   100% error rate    |
| M31  |     Lang_32      |   100% error rate    |
| M32  |     Lang_35      |   100% error rate    |
| M33  |     Lang_37      |   100% error rate    |
| M34  |     Lang_40      |   100% error rate    |
| M35  |     Lang_42      |   100% error rate    |
| M36  |     Lang_47      |   100% error rate    |
| M37  |     Lang_50      |   100% error rate    |
| M38  |     Lang_56      |   100% error rate    |
| M39  |     Lang_63      |   100% error rate    |
| M40  |    Math_4j_3     |   100% error rate    |
| M41  |    Math_4j_4     |   100% error rate    |
| M42  |    Math_4j_5     |   100% error rate    |
| M43  |    Math_4j_6     |   100% error rate    |
| M44  |    Math_4j_7     |   100% error rate    |
| M45  |    Math_4j_8     |   100% error rate    |
| M46  |    Math_4j_12    |   100% error rate    |
| M47  |    Math_4j_13    |   100% error rate    |
| M48  |    Math_4j_14    |   100% error rate    |
| M49  |    Math_4j_18    |   100% error rate    |
| M50  |    Math_4j_19    |   100% error rate    |
| M51  |    Math_4j_20    |   100% error rate    |
| M52  |    Math_4j_22    |   100% error rate    |
| M53  |    Math_4j_23    |   100% error rate    |
| M54  |    Math_4j_24    |   100% error rate    |
| M55  |    Math_4j_25    |   100% error rate    |
| M56  |    Math_4j_28    |   100% error rate    |
| M57  |    Math_4j_29    |   100% error rate    |
| M58  |    Math_4j_35    |   100% error rate    |
| M59  |    Math_4j_36    |   100% error rate    |
| M60  |    Math_4j_37    |   100% error rate    |
| M61  |    Math_4j_38    |   100% error rate    |
| M62  |    Math_4j_39    |   100% error rate    |
| M63  |    Math_4j_40    |   100% error rate    |
| M64  |    Math_4j_44    |   100% error rate    |
| M65  |    Math_4j_45    |   100% error rate    |
| M66  |    Math_4j_46    |   100% error rate    |
| M67  |    Math_4j_50    |   100% error rate    |
| M68  |    Math_4j_51    |   100% error rate    |
| M69  |    Math_4j_52    |   100% error rate    |
| M70  |    Math_4j_54    |   100% error rate    |
| M71  |    Math_4j_55    |   100% error rate    |
| M72  |    Math_4j_56    |   100% error rate    |
| M73  |    Math_4j_57    |   100% error rate    |
| M74  |    Math_4j_60    |   100% error rate    |
| M75  |    Math_4j_61    |   100% error rate    |
| M76  |    Math_4j_67    |   100% error rate    |
| M77  |    Math_4j_68    |   100% error rate    |
| M78  |    Math_4j_69    |   100% error rate    |
| M79  |    Math_4j_70    |   100% error rate    |
| M80  |    Math_4j_71    |   100% error rate    |
| M81  |    Math_4j_72    |   100% error rate    |
| M82  |    Math_4j_76    |   100% error rate    |
| M83  |    Math_4j_77    |   100% error rate    |
| M84  |    Math_4j_78    |   100% error rate    |
| M85  |    Math_4j_82    |   100% error rate    |
| M86  |    Math_4j_83    |   100% error rate    |
| M87  |    Math_4j_84    |   100% error rate    |
| M88  |    Math_4j_86    |   100% error rate    |
| M89  |    Math_4j_87    |   100% error rate    |
| M90  |    Math_4j_89    |   100% error rate    |
| M91  |    Math_4j_92    |   100% error rate    |
| M92  |    Math_4j_93    |   100% error rate    |
| M93  |    Math_4j_99    |   100% error rate    |
| M94  |   Math_4j_100    |   100% error rate    |
| M95  |   Math_4j_101    |   100% error rate    |
| M96  |   Math_4j_102    |   100% error rate    |
| M97  |   Math_4j_103    |   100% error rate    |
| M98  |   Math_4j_104    |   100% error rate    |
| M99  |    Closure_1     |   100% error rate    |
| M100 |    Closure_2     |   100% error rate    |
| M101 |    Closure_4     |   100% error rate    |
| M102 |    Closure_5     |   100% error rate    |
| M103 |    Closure_6     |   100% error rate    |
| M104 |    Closure_7     |   100% error rate    |
| M105 |    Closure_8     |   100% error rate    |
| M106 |    Closure_10    |    external files    |
| M107 |    Closure_11    |    external files    |
| M108 |    Closure_12    |    external files    |
| M109 |    Closure_13    |    external files    |
| M110 |    Closure_14    |    external files    |
| M111 |    Closure_16    |   100% error rate    |
| M112 |    Closure_18    |   100% error rate    |
| M113 |    Closure_21    |   100% error rate    |
| M114 |    Closure_22    |   100% error rate    |
| M115 |    Closure_24    |   100% error rate    |
| M116 |    Closure_25    |   100% error rate    |
| M117 |    Closure_30    |    external files    |
| M118 |    Closure_31    |    external files    |
| M119 |    Closure_34    |    external files    |
| M120 |    Closure_36    |   100% error rate    |
| M121 |    Closure_38    |   100% error rate    |
| M122 |    Closure_42    |   100% error rate    |
| M123 |    Closure_43    |   100% error rate    |
| M124 |    Closure_45    |   100% error rate    |
| M125 |    Closure_46    |   100% error rate    |
| M126 |    Closure_47    |   100% error rate    |
| M127 |    Closure_48    |   100% error rate    |
| M128 |    Closure_49    |   100% error rate    |
| M129 |    Closure_51    |    external files    |
| M130 |    Closure_52    |    external files    |
| M131 |    Closure_53    |    external files    |
| M132 |    Closure_54    |    external files    |
| M133 |    Closure_55    |    external files    |
| M134 |    Closure_59    |   100% error rate    |
| M135 |    Closure_60    |   100% error rate    |
| M136 |    Closure_61    |   100% error rate    |
| M137 |    Closure_63    |   100% error rate    |
| M138 |    Closure_64    |   100% error rate    |
| M139 |    Closure_66    |   100% error rate    |
| M140 |    Closure_69    |   100% error rate    |
| M141 |    Closure_70    |   100% error rate    |
| M142 |    Closure_72    |   100% error rate    |
| M143 |    Closure_73    |   100% error rate    |
| M144 |    Closure_74    |   100% error rate    |
| M145 |    Closure_75    |   100% error rate    |
| M146 |    Closure_76    |   100% error rate    |
| M147 |    Closure_78    |    external files    |
| M148 |    Closure_79    |    external files    |
| M149 |    Closure_80    |    external files    |
| M150 |    Closure_81    |    external files    |
| M151 |    Closure_82    |    external files    |
| M152 |    Closure_84    |   100% error rate    |
| M153 |    Closure_86    |   100% error rate    |
| M154 |    Closure_90    |   100% error rate    |
| M155 |    Closure_92    |   100% error rate    |
| M156 |    Closure_93    |   100% error rate    |
| M157 |    Closure_94    |   100% error rate    |
| M158 |    Closure_95    |   100% error rate    |
| M159 |    Closure_96    |   100% error rate    |
| M160 |    Closure_98    |    external files    |
| M161 |    Closure_99    |    external files    |
| M162 |   Closure_100    |    external files    |
| M163 |   Closure_104    |   100% error rate    |
| M164 |   Closure_106    |   100% error rate    |
| M165 |   Closure_110    |   100% error rate    |
| M166 |   Closure_111    |   100% error rate    |
| M167 |   Closure_113    |   100% error rate    |
| M168 |   Closure_119    |    external files    |
| M169 |   Closure_120    |    external files    |
| M170 |   Closure_121    |    external files    |
| M171 |   Closure_122    |    external files    |
| M172 |   Closure_123    |    external files    |
| M173 |   Closure_127    |   100% error rate    |
| M174 |   Closure_128    |   100% error rate    |
| M175 |   Closure_129    |   100% error rate    |
| M176 |   Closure_131    |   100% error rate    |
| M177 |   Closure_132    |   100% error rate    |
