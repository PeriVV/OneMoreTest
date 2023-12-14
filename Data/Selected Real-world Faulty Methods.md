
## Selected Real-world Faulty Methods
|   ID   |      Method Signature     |  Size(LOC)   | # Invoked Methods  |
|:------:|:----------------------------:|:-------:|:-------:|
|   M1   | TimeSeries createCopy(RegularTimePeriod start, RegularTimePeriod end) | 38 | 9 |
|   M2   | XYDataItem addOrUpdate(Number x, Number y) | 37 | 9 |
|   M3   | void updateBounds(TimePeriod period, int index) | 78 | 32 |
|   M4   | TimeSeries createCopy(RegularTimePeriod start, RegularTimePeriod end) | 38 | 9 |
|   M5   | Size2D arrangeFF(BlockContainer container, Graphics2D g2, <br/> RectangleConstraint constraint) | 67 | 22 |
|   M6   | DefaultIntervalCategoryDataset(Comparable[] seriesKeys, <br/> Comparable[] categoryKeys,Number[][] starts,Number[][] ends) | 70 | 8 |
|   M7   | void removeColumn(Comparable columnKey) | 7 | 5 |
|   M8   | ValueMarker(double value, Paint paint, Stroke stroke, <br/>Paint outlinePaint, Stroke outlineStroke, float alpha) | 4 | 1 |
|   M9   | DefaultBoxAndWhiskerCategoryDataset() | 9 | 2 |
|   M10  | void removeObject(Comparable rowKey, Comparable columnKey) | 24 | 5 |
|   M11  | boolean equals(Object obj) | 19 | 2 |
|   M12  | void addYears(int) | 3 | 5 |
|   M13  | void addMonths(int) | 3 | 5 |
|   M14  | void addWeeks(int) | 3 | 5 |
|   M15  | void addDays(int) | 3 | 5 |
|   M16  | Partial with(DateTimeFieldType fieldType, int value) | 48 | 24 |
|   M17  | GJChronology getInstance(DateTimeZone zone, <br/> ReadableInstant gregorianCutover,int minDaysInFirstWeek) | 45 | 13 |
|   M18  | int parseInto(ReadWritableInstant instant, <br/>String text, int position) | 28 | 19 |
|   M19  | MutableDateTime parseMutableDateTime(String text) | 26  | 16 |
|   M20  | DateTimeZone forOffsetHoursMinutes(int hoursOffset, int minutesOffset) | 23 | 5 |
|   M21  | int between(ReadablePartial start, ReadablePartial end, <br/>ReadablePeriod zeroInstance) | 18 | 16 |
|   M22  | LocalDateTime fromDateFields(Date date) | 14 | 9 |
|   M23  | MonthDay minusMonths(int) | 3 | 3 |
|   M24  | MonthDay plusMonths(int) | 3 | 2 |
|   M25  | long safeMultiply(long val1, int val2) | 15 | 1 |
|   M26  | long adjustOffset(long instant, boolean earlierOrLater) | 17 | 4 |
|   M27  | long getDateTimeMillis(int year, int monthOfYear, int dayOfMonth, int millisOfDay) | 22 | 4 |
|   M28  | Period parsePeriod(String text) | 4 | 3 |
|   M29  | long computeMillis(boolean resetFields, String text) | 47 | 12 |
|   M30  | long add(long instant, int value) | 10 | 5 |
|   M31  | PeriodFormatter toFormatter(List<Object> elementPairs, <br/>boolean notPrinter, boolean notParser) | 19 | 13 |
|   M32  | Number createNumber(String str) | 158 | 55 |
|   M33  | translate(CharSequence input, Writer out) | 23 | 6 |
|   M34  | Number createNumber(String str) | 153 | 53 |
|   M35  | void appendTo(StringBuffer buffer, Calendar calendar) | 7 | 6 |
|   M36  | void init() | 36 | 21 |
|   M37  | String random(int count, int start, int end, boolean letters, <br/>boolean numbers, char[] chars, Random random) | 65 | 9 |
|   M38  | String random(int count, int start, int end, boolean letters, <br/>boolean numbers, char[] chars, Random random) | 60 | 8 |
|   M39  | void translate(CharSequence input, Writer out) | 29 | 6 |
|   M40  | int translate(CharSequence input, int index, Writer out) | 44 | 14 |
|   M41  | boolean isSameLocalTime(Calendar cal1, Calendar cal2) | 12 | 17 |
|   M42  | int greatestCommonDivisor(int u, int v) | 44  | 3 |
|   M43  | String format(Date date) | 4 | 5 |
|   M44  | Number createNumber(String str) | 150 | 47 |
|   M45  | int translate(CharSequence input, int index, Writer out) | 32 | 11 |
|   M46  | boolean isNumber(String str) | 94  | 2 |
|   M47  | StringBuffer format(Calendar calendar, StringBuffer buf) | 6 | 3 |
|   M48  | String replaceEach(String text, String[] searchList, <br/>String[] replacementList,  boolean repeat, int timeToLive)  | 126 | 13 |
|   M49  | String getShortClassName(String className) | 19 | 4 |
|   M50  | StringBuffer appendQuotedString(String pattern, ParsePosition pos, <br/>StringBuffer appendTo, boolean escapingOn) | 28 | 15 |
|   M51  | Number createNumber(String val) | 148 | 48 |
|   M52  | String abbreviate(String str, int lower, int upper, String appendToEnd) | 38 | 17 |
|   M53  | String escapeJava(String str) | 3 | 1 |
|   M54  | EqualsBuilder append(Object lhs, Object rhs) | 42 | 14 |
|   M55  | Fraction reduce() | 9 | 3 |
|   M56  | void modify(Calendar val, int field, boolean round) | 126 | 18 |
|   M57  | Locale toLocale(String str) | 36 | 18 |
|   M58  | boolean isAvailableLocale(Locale locale) | 2 | 2 |
|   M59  | Number createNumber(String str) | 147 | 48 |
|   M60  | StrBuilder appendFixedWidthPadRight(Object obj, int width, char padChar) | 17 | 6 |
|   M61  | int indexOf(String str, int startIndex) | 27 | 3 |
|   M62  | int getValueInOtherClassLoader(Object other) | 13 | 5 |
|   M63  | void modify(Calendar val, int field, boolean round) | 77 | 13 |
|   M64  | BigFraction(final double value, final double epsilon, <br/>final int maxDenominator, int maxIterations) | 66 | 9 |
|   M65  | getNumericalMean() | 3 | 3 |
|   M66  | Line revert() | 3 | 1 |
|   M67  | void atan2(final double[] y, final int yOffset, final double[] x, <br/>final int xOffset, final double[] result, final int resultOffset) | 38 | 12 |
|   M68  | double density(final double[] vals) | 9 | 5 |
|   M69  | double cosh(double x) | 54 | 3 |
|   M70  | Dfp multiply(final int x) | 3 | 1 |
|   M71  | RectangularCholeskyDecomposition(RealMatrix matrix, double small) | 89 | 7 |
|   M72  | Fraction(double value, double epsilon, int maxDenominator, int maxIterations) | 63 | 7 |
|   M73  | double percentageValue() | 3 | 2 |
|   M74  | double calculateAsymptoticPValue(final double Umin,  final int n1, final int n2) | 16 | 3 |
|   M75  | int inverseCumulativeProbability(final double p) | 43 | 14 |
|   M76  | void dropPhase1Objective() | 40 | 14 |
|   M77  | Iterator<Chromosome> iterator() | 3 | 1 |
|   M78  | double evaluate(final double[] values, final double[] weights, <br/>final double mean, final int begin, final int length) | 31 | 1 |
|   M79  | RealPointValuePair getSolution() | 29 | 12 |
|   M80  | final double doSolve() | 122 | 14 |
|   M81  | OpenMapRealVector ebeDivide(RealVector v) | 9 | 8 |
|   M82  | Complex add(Complex rhs) | 5 | 4 |
|   M83  | double[] fit() | 4 | 4 |
|   M84  | float max(final float a, final float b) | 3 | 1 |
|   M85  | UnivariateRealPointValuePair optimize(final FUNC f, final GoalType goal, <br/>final double min, final double max, final double startValue) | 33 | 8 |
|   M86  | boolean equals(double x, double y) | 3 | 2 |
|   M87  | double getRMS() | 7 | 0 |
|   M88  | double integrate(final FirstOrderDifferentialEquations equations, <br/>final double t0, final double[] y0, final double t, final double[] y) | 167 | 36 |
|   M89  | double getPct(Comparable<?> v) | 6 | 2 |
|   M90  | boolean flipIfWarranted(final int n, final int step) | 15 | 0 |
|   M91  | void processGeneralBlock(final int n) | 106 | 8 |
|   M92  | void addValue(Object v) | 27 | 9 |
|   M93  | int compareTo(Fraction object) | 4 | 2 |
|   M94  | int gcd(int u, int v) | 49 | 3 |
|   M95  | void setDenominatorDegreesOfFreedom(double degreesOfFreedom) | 6 | 1 |
|   M96  | boolean equals(Object other) | 22 | 7 |
|   M97  | double solve(double min, double max) | 27 | 6 |
|   M98  | BigDecimal[] operate(BigDecimal[] v) | 15 | 3 |
|   M99  | double getSumSquaredErrors() | 3 | 0 |
|   M100  | Fraction parse(String source, ParsePosition pos) | 76 | 26 |
|   M101  | void removeUnreferencedFunctionArgs(Scope fnScope) | 29 | 9 |
|   M102  | Node tryFoldSimpleFunctionCall(Node n) | 22 | 14 |
|   M103  | Node tryFoldArrayAccess(Node n, Node left, Node right) | 50 | 11 |
|   M104  | void emitOptionalModuleExportsOverride<br/>(Node script, String moduleName) | 10 | 10 |
|   M105  | Node tryFinally(Node tryBody, Node finallyBody) | 5 | 6 |
|   M106  | void traverseFunction(Node n, Node parent) | 35 | 13 |
|   M107  | void visit(NodeTraversal t, Node n, Node parent) | 42 | 22 |
|   M108  | FunctionTypeBuilder inferFromOverriddenFunction <br/>(@Nullable FunctionType oldType, @Nullable Node paramsParent) | 54 | 21 |
|   M109  | void add(String newcode) | 21 | 5 |
|   M110  | String extractClassNameIfGoog(Node node, <br/>Node parent, String functionName) | 16 | 7 |
|   M111  | computeGenKill(Node n, BitSet gen, BitSet kill, boolean conditional) | 85 | 35 |
|   M112  | boolean isPrototypePropertyAssign(Node assign) | 20 | 11 |
|   M113  | Node parseBasicTypeExpression(JsDocToken token) | 25 | 19 |
|   M114  | void checkPropertyVisibility(NodeTraversal t, Node getprop, Node parent) | 93 | 26 |
|   M115  | Node tryRemoveUnconditionalBranching(Node n) | 62 | 22 |
|   M116  | VariableLiveness isVariableReadBeforeKill(Node n, String variable) | 11 | 4 |
|   M117  | boolean shouldTraverse(NodeTraversal t, Node n, Node parent) | 64 | 20 |
|   M118  | void tryFoldStringJoin(NodeTraversal t, Node n, <br/>Node left, Node right, Node parent) | 88 | 14 |
|   M119  | void exitScope(NodeTraversal t) | 13 | 5 |
|   M120  | Node parseContextTypeExpression(JsDocToken token) | 3 | 1 |
|   M121  | boolean inferTemplatedTypesForCall(<br/>Node n, FunctionType fnType) | 27 | 11 |
|   M122  | void recordAssignment(NodeTraversal t, Node n, Node recordNode) | 30 | 9 |
|   M123  | Node inlineReturnValue(Node callNode, Node fnNode) | 31 | 15 |
|   M124  | String getReadableJSTypeName(Node n, boolean dereference) | 53 | 24 |
|   M125  | void visitNew(NodeTraversal t, Node n) | 15 | 11 |
|   M126  | void tryMinimizeExits(Node n, int exitType, String labelName) | 95 | 33 |
|   M127  | void escapeJavaStyleString(Writer out, String str, boolean escapeSingleQuote) | 75 | 25 |
|   M128  | Range iterateDomainBounds(XYDataset dataset,  boolean includeInterval) | 45 | 13 |
|   M129  | RealPointValuePair getSolution() | 21 | 9 |
|   M130  | String getRemainingJSDocLine() | 4 | 1 |
|   M131  | int parseArguments(Parameters params) | 19  | 7 |
|   M132  | DateTimeZone forOffsetHoursMinutes(int hoursOffset, int minutesOffset) | 20 | 7 |
|   M133  | void printTo(StringBuffer buf, ReadablePeriod period, Locale locale) | 29 | 8 |
|   M134  | boolean isNumber(String str) | 102 | 2 |
|   M135  | static Class<?>[] toClass(Object[] array) | 11 | 0 |
|   M136  | String generateToolTipFragment(String toolTipText) | 3 | 0 |
|   M137  | Class<?>[] toClass(Object[] array) | 11 | 1 |
|   M138  | double[] bracket(UnivariateRealFunction function,double initial, <br/>double lowerBound, double upperBound, int maximumIterations) | 43 | 4 |
|   M139  | String format(JSError error, boolean warning) | 45 | 23 |
|   M140  | void inlineAliases(GlobalNamespace namespace) | 36 | 9 |
|   M141  | boolean contains(char ch) | 8 | 0 |
|   M142  | boolean toBoolean(String str) | 51 | 23 |
|   M143  | void unescape(Writer writer, String string) | 66 | 21 |
|   M144  | boolean isSupportUpperBoundInclusive() | 3 | 0 |
|   M145  | FastDateFormat getDateInstance(int style, TimeZone timeZone, Locale locale) | 25 | 10 |
|   M146  | LegendItemCollection getLegendItems() | 32 | 10 |
|   M147  | boolean mayThrowException(Node n) | 20 | 5 |
|   M148  | void declareNameInScope(FlowScope scope, Node node, JSType type) | 23 | 10 |
|   M149  | boolean isFoldableExpressBlock(Node n) | 19 | 3 |
|   M150  | String toStringHelper(boolean forAnnotations) | 43 | 14 |
|   M151  | CompilerOptions createOptions() | 56 | 17 |
|   M152  | String getLine(int lineNumber) | 41 | 5 |
|   M153  | String normalizeSourceName(String filename) | 10 | 2 |
|   M154  | boolean isInlinableObject(List<Reference> refs) | 85 | 17 |
|   M155  | Node tryFoldArrayJoin(Node n) | 109 | 47 |
|   M156  | String strEscape(String s, char quote, String doublequoteEscape, <br/>String singlequoteEscape, String backslashEscape, CharsetEncoder outputCharsetEncoder) | 69 | 11 |
|   M157  | Node tryFoldShift(Node n, Node left, Node right) | 61 | 12 |
|   M158  | void handleObjectLit(NodeTraversal t, Node n) | 23 | 13 |
|   M159  | Complex atan() | 7 | 7 |
|   M160  | List<Cluster<T>> cluster(final Collection<T> points, <br/>final int k, final int maxIterations) | 25 | 7 |
|   M161  | Complex divide(Complex divisor) | 29 | 8 |
|   M162  | double distance(int[] p1, int[] p2) | 7 | 1 |
|   M163  | StringBuilder escapeRegex(StringBuilder regex, String value, boolean unquote) | 40 | 6 |
|   M164  | Number createNumber(String str) | 150 | 45 |
|   M165  | String join(Object[] array, char separator, <br/>int startIndex, int endIndex) | 19 | 6 |
|   M166  | float toJavaVersionInt(String version) | 3 | 2 |
|   M167  | void stop() | 6 | 1 |
|   M168  | void computeGeometricalProperties() | 51 | 16 |
|   M169  | void addValue(double value) | 19 | 9 |
|   M170  | CanInlineResult canInlineReferenceDirectly(Node callNode, Node fnNode) | 69 | 17 |
|   M171  | Paint getPaint(double value) | 6 | 3 |
|   M172  | boolean equals(CharSequence cs1, CharSequence cs2) | 9 | 1 |
|   M173  | double pow(double x, double y) | 158 | 6 |
|   M174  | VectorialPointValuePair doOptimize() | 223 | 20 |
|   M175  | double localMin(boolean isMinim,  UnivariateRealFunction f, <br/>GoalType goalType, double lo, double mid, double hi, double eps, double t) | 151 | 6 |
|   M176  | double solve(final UnivariateRealFunction f, final double min, <br/>final double max, final double initial) | 42 | 13 |
|   M177  | JSType getDeclaredType(String sourceName, JSDocInfo info, <br/>Node lValue, @Nullable Node rValue) | 50 | 25 |
|   M178  | String strEscape(String s, char quote, String doublequoteEscape, <br/>String singlequoteEscape, String backslashEscape, CharsetEncoder outputCharsetEncoder) | 70 | 21 |
