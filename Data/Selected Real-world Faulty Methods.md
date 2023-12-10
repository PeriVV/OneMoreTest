
## Selected Real-world Faulty Methods
|   ID   |      Method Signature     |  Size(LOC)   | # Invoked Methods  |
|:------:|:----------------------------:|:-------:|:-------:|
|   M1   | void setMaximumItemAge(long periods) | 7 | 2 |
|   M2   | TimeSeries createCopy(int start, int end) | 24 | 7 |
|   M3   | XYDataItem addOrUpdate(Number x, Number y) | 36 | 8 |
|   M4   | void updateBounds(TimePeriod period, int index) | 78 | 19 |
|   M5   | Size2D arrangeFF(BlockContainer container, Graphics2D g2, <br/> RectangleConstraint constraint) | 67 | 21 |
|   M6   | void setCategoryKeys(Comparable[] categoryKeys) | 18 | 4 |
|   M7   | void addValue(double value, Comparable rowKey, <br/>Comparable columnKey) | 4 | 1 |
|   M8   | ValueMarker(double value, Paint paint, Stroke stroke, <br/>Paint outlinePaint, Stroke outlineStroke, float alpha) | 4 | 0 |
|   M9   | void updateBounds() | 3 | 0 |
|   M10  | void removeColumn(Comparable columnKey) | 12 | 6 |
|   M11  | void setDrawLines(boolean draw) | 5 | 2 |
|   M12  | void addYears(int) | 5  | 4 |
|   M13  | void addMonths(int) | 5  | 4 |
|   M14  | void addWeeks(int) | 5  | 4 |
|   M15  | void addDays(int) | 5  | 4 |
|   M16  | int get(DateTimeFieldType type) | 3 | 2 |
|   M17  | LocalDate addToCopy(int value) | 3 | 3 |
|   M18  | int parseInto(ReadWritableInstant instant, <br/>String text, int position) | 28 | 14 |
|   M19  | int mutableDateTime(ReadWritableInstant instant, <br/>String text, int position) | 28  | 14 |
|   M20  | DateTimeZone forOffsetHoursMinutes <br/> (int hoursOffset, int minutesOffset) | 23 | 3 |
|   M21  | Days daysBetween(ReadablePartial start, <br/>ReadablePartial end) | 10 | 7 |
|   M22  | LocalDateTime fromDateFields(Date date) | 14 | 9 |
|   M23  | MonthDay minusMonths(int) | 9 | 6 |
|   M24  | MonthDay plusMonths(int) | 9 | 6 |
|   M25  | long safeMultiply(long val1, int val2) | 14 | 1 |
|   M26  | DateTime withLaterOffsetAtOverlap() | 4 | 4 |
|   M27  | int getDayOfMonth() | 3 | 4 |
|   M28  | Period toPeriod() | 3 | 2 |
|   M29  | LocalDate parseLocalDate(String text) | 3  | 2 |
|   M30  | DateTime withSecondOfMinute(int second) | 3 | 5 |
|   M31  | Period parsePeriod(String text) | 4  | 3 |
|   M32  | Number createNumber(String str) | 157 | 21 |
|   M33  | String escapeCsv(String input) | 3 | 1 |
|   M34  | void appendTo(StringBuffer buffer, Calendar calendar) | 7 | 6 |
|   M35  | void setTimeZone(TimeZone zone) | 3 | 1 |
|   M36  | Date parse(String source) | 3 | 1 |
|   M37  | String random(int count, int start, int end, <br/>boolean letters, boolean numbers) | 3 | 1 |
|   M38  | String random(int count, String chars) | 5 | 2 |
|   M39  | String escapeXml(String input) | 3 | 1 |
|   M40  | String translate(CharSequence input) | 12  | 4 |
|   M41  | boolean isSameLocalTime(Calendar cal1, Calendar cal2) | 12 | 4 |
|   M42  | Fraction getReducedFraction(int numerator, int denominator) | 25  | 3 |
|   M43  | FastDateFormat getInstance(String pattern, Locale locale) | 3 | 1 |
|   M44  | int translate(final CharSequence input, final int index, final Writer out) | 32 | 7 |
|   M45  | String translate(CharSequence input) | 12 | 5 |
|   M46  | Number createNumber(String str) | 147  | 19 |
|   M47  | String format(Calendar calendar) | 3 | 3 |
|   M48  | String replaceEach(String text, <br/>String[] searchList, String[] replacementList) | 3 | 1 |
|   M49  | String getShortClassName(Class<?> cls) | 6 | 2 |
|   M50  | String format (Object obj) | 3 | 4 |
|   M51  | NumberUtils() | 3 | 1 |
|   M52  | String abbreviate(String str, int lower, <br/>int upper, String appendToEnd) | 38 | 7 |
|   M53  | String escapeJava(String str) | 3 | 1 |
|   M54  | Number createNumber(String str) | 150 | 23 |
|   M55  | Fraction reduce() | 9 | 3 |
|   M56  | Date round(Date date, int field) | 8 | 5 |
|   M57  | Locale toLocale(String str) | 36 | 10 |
|   M58  | HashSet(Collection<? extends E> c) | 4 | 3 |
|   M59  | boolean isNumber(String str) | 94 | 2 |
|   M60  | StrBuilder appendFixedWidthPadLeft(int value, <br/>int width, char padChar) | 3 | 2 |
|   M61  | int indexOf(String str) | 3 | 1 |
|   M62  | int compareTo(Object other) | 12 | 10 |
|   M63  | String format(Date date) | 4 | 3 |
|   M64  | BigFraction(final double value, final int maxDenominator) | 3 | 1 |
|   M65  | int sample() | 3 | 2 |
|   M66  | Line revert() | 4 | 2 |
|   M67  | double getValue() | 2 | 0 |
|   M68  | MultivariateNormalDistribution(final double[] means, <br/>final double[][] covariances) | 6 | 2 |
|   M69  | double max(final double a, final double b) | 19 | 1 |
|   M70  | Dfp newDfp(final String s) | 2 | 1 |
|   M71  | RealVector subtract(RealVector v) | 10 | 9 |
|   M72  | Fraction(double value, double epsilon, int maxIterations) | 4 | 1 |
|   M73  | double percentageValue() | 3 | 2 |
|   M74  | double mannWhitneyUTest(final double[] x, final double[] y) | 14 | 3 |
|   M75  | int inverseCumulativeProbability(final double p) | 43 | 14 |
|   M76  | PointValuePair optimize(final LinearObjectiveFunction f,<br/>final Collection<LinearConstraint> constraints,<br/>final GoalType goalType, final boolean restrictToNonNegative) | 31 | 0 |
|   M77  | Iterator<Chromosome> iterator() | 3 | 1 |
|   M78  | evaluate(final double[] values, final double[] weights, <br/>final double mean, final int begin, final int length) | 12 | 4 |
|   M79  | RealPointValuePair optimize(final LinearObjectiveFunction f, <br/>final Collection <LinearConstraint> constraints, <br/>final GoalType goalType, final boolean restrictToNonNegative) | 16 | 1 |
|   M80  | double solve(int maxEval, FUNC f, double min, double max, double startValue) | 6  | 2 |
|   M81  | RealVector ebeMultiply(RealVector v) | 11 | 4 |
|   M82  | Complex add(Complex rhs) | 5 | 4 |
|   M83  | void addObservedPoint(double x, double y) | 3 | 1 |
|   M84  | float max(final float a, final float b) | 3 | 1 |
|   M85  | UnivariateRealPointValuePair[] getOptima() | 5 | 2 |
|   M86  | double nextAfter(double d, double direction) | 38 | 6 |
|   M87  | double[][] getCovariances() | 28 | 7 |
|   M88  | double integrate(final FirstOrderDifferentialEquations equations, <br/>final double t0, final double[] y0, final double t, final double[] y) | 158 | 25 |
|   M89  | double getPct(Comparable<?> v) | 6 | 2 |
|   M90  | EigenDecompositionImpl(final double[] main, double[] secondary,<br/>final double splitTolerance) | 18 | 3 |
|   M91  | RealVector subtract(RealVector v) | 12 | 4 |
|   M92  | void addValue(Object v) | 28 | 6 |
|   M93  | int compareTo(Fraction object) | 4 | 2 |
|   M94  | int gcd(int u, int v) | 49 | 2 |
|   M95  | void setDenominatorDegreesOfFreedom(double degreesOfFreedom) | 6 | 1 |
|   M96  | Complex tanh() | 10 | 6 |
|   M97  | double solve(double min, double max) | 79 | 8 |
|   M98  | double doubleValue() | 26 | 3 |
|   M99  | double getSumSquaredErrors() | 3 | 0 |
|   M100  | Fraction parse(String source) | 8 | 4 |
|   M101  | void removeUnreferencedFunctionArgs(Scope fnScope) | 29 | 9 |
|   M102  | Node tryFoldSimpleFunctionCall(Node n) | 22 | 14 |
|   M103  | Node tryFoldArrayAccess(Node n, Node left, Node right) | 50 | 11 |
|   M104  | void emitOptionalModuleExportsOverride<br/>(Node script, String moduleName) | 10 | 10 |
|   M105  | Node tryFinally(Node tryBody, Node finallyBody) | 5 | 6 |
|   M106  | void traverseFunction(Node n, Node parent) | 35 | 13 |
|   M107  | void visit(NodeTraversal t, Node n, Node parent) | 42 | 22 |
|   M108  | FunctionTypeBuilder inferFromOverriddenFunction<br/>(@Nullable FunctionType oldType, @Nullable Node paramsParent) | 54 | 21 |
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
|   M127  | String escapeJavaScript(String str) | 3 | 1 |
|   M128  | double getLowerBound() | 3 | 0 |
|   M129  | double[] getPoint() | 3 | 1 |
|   M130  | String getRemainingJSDocLine() | 4 | 1 |
|   M131  | int parseArguments(Parameters params) | 19  | 7 |
|   M132  | boolean isNumber(String str) | 102 | 2 |
|   M133  | void addIdentifier(String identifier) | 3 | 1 |
|   M134  | String generateToolTipFragment(String toolTipText) | 4 | 0 |
|   M135  | static Class<?>[] toClass(Object[] array) | 11 | 0 |
|   M136  | double inverseCumulativeProbability(final double p) | 51 | 12 |
|   M137  | String format(JSError error, boolean warning) | 45 | 22 |
|   M138  | void inlineAliases(GlobalNamespace namespace) | 36 | 7 |
|   M139  | boolean contains(char ch) | 8 | 0 |
|   M140  | boolean toBoolean(String str) | 51 | 24 |
|   M141  | String unescape(String str) | 60 | 14 |
|   M142  | double density(double x) | 11 | 4 |
|   M143  | FastDateFormat getInstance(String pattern, Locale locale) | 3 | 1 |
|   M144  | int getLegendItems() | 32 | 11 |
|   M145  | Predicate<Node>() | 29 | 6 |
|   M146  | void inferPropertyTypesToMatchConstraint<br/>(JSType type, JSType constraint) | 24 | 12 |
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
|   M161  | DateTimeZone forOffsetHoursMinutes <br/> (int hoursOffset, int minutesOffset) | 20 | 4 |
|   M162  | PeriodFormatter standard() | 22 | 12 |
|   M163  | void setTimeZone(TimeZone zone) | 3 | 1 |
|   M164  | Number createNumber(String str) | 150 | 18 |
|   M165  | String join(Object[] array, char separator, <br/>int startIndex, int endIndex) | 19 | 5 |
|   M166  | float toJavaVersionInt(String version) | 3 | 2 |
|   M167  | long getTime() | 11 | 2 |
|   M168  | double getBoundarySize() | 4 | 3 |
|   M169  | void checkTheoreticalMinCost(double rms) | 4 | 1 |
|   M170  | Node inlineReturnValue(Node callNode, Node fnNode) | 31 | 11 |
|   M171  | Paint getPaint(double value) | 6 | 3 |
|   M172  | boolean equals(CharSequence cs1, CharSequence cs2) | 9 | 1 |
|   M173  | double pow(double x, double y) | 158 | 4 |
|   M174  | double getMean() | 3 | 1 |
|   M175  | double doOptimize() | 3 | 1 |
|   M176  | double solve(final UnivariateRealFunction f, final double min, <br/>final double max, final double initial) | 42 | 8 |
|   M177  | JSType getDeclaredType(String sourceName, JSDocInfo info, <br/>Node lValue, @Nullable Node rValue) | 50 | 22 |
|   M178  | String strEscape(String s, char quote, String doublequoteEscape, <br/>String singlequoteEscape, String backslashEscape, CharsetEncoder outputCharsetEncoder) | 70 | 21 |
