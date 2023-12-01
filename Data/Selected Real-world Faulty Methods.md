
## Selected Real-world Faulty Methods
|   ID   |      Method Signature     |  Size(LOC)   | # Invoked Methods  |
|:------:|:----------------------------:|:-------:|:-------:|
|   M1   | int getItemCount() | 3 | 1 |
|   M2   | void setMaximumItemAge(long periods) | 7 | 2 |
|   M3   | Number getY(int index) | 3 | 1 |
|   M4   | int getMaxMiddleIndex() | 3 | 0 |
|   M5   | TimeSeries createCopy(RegularTimePeriod start, <br/>RegularTimePeriod end) | 38 | 4 |
|   M6   | Size2D arrange(Graphics2D g2, <br/>RectangleConstraint constraint) | 3 | 1 |
|   M7   | int getCategoryIndex(Comparable category) | 10 | 1 |
|   M8  | void addValue(double value, Comparable rowKey, <br/>Comparable columnKey) | 4 | 1 |
|   M9  | Paint getOutlinePaint() | 3 | 3 |
|   M10  | Range getRangeBounds(boolean includeInterval) | 3 | 0 |
|   M11  | void removeColumn(Comparable columnKey) | 12 | 6 |
|   M12  | void setDrawLines(boolean draw) | 5 | 2 |
|   M13  | void addYears(int) | 5  | 4 |
|   M14  | void addMonths(int) | 5  | 4 |
|   M15  | void addWeeks(int) | 5  | 4 |
|   M16  | void addDays(int) | 5  | 4 |
|   M17  | int get(DateTimeFieldType type) | 3 | 2 |
|   M18  | LocalDate addToCopy(int value) | 3 | 3 |
|   M19  | int parseInto(ReadWritableInstant instant, <br/>String text, int position) | 28 | 14 |
|   M20  | int mutableDateTime(ReadWritableInstant instant, <br/>String text, int position) | 28  | 14 |
|   M21  | DateTimeZone forOffsetHoursMinutes <br/> (int hoursOffset, int minutesOffset) | 23 | 3 |
|   M22  | Days daysBetween(ReadablePartial start, <br/>ReadablePartial end) | 10 | 7 |
|   M23  | LocalDateTime fromDateFields(Date date) | 14 | 9 |
|   M24  | MonthDay minusMonths(int) | 9 | 6 |
|   M25  | MonthDay plusMonths(int) | 9 | 6 |
|   M26  | long safeMultiply(long val1, int val2) | 14 | 1 |
|   M27  | DateTime withLaterOffsetAtOverlap() | 4 | 4 |
|   M28  | int getDayOfMonth() | 3 | 4 |
|   M29  | Period toPeriod() | 3 | 2 |
|   M30  | LocalDate parseLocalDate(String text) | 3  | 2 |
|   M31  | DateTime withSecondOfMinute(int second) | 3 | 5 |
|   M32  | Period parsePeriod(String text) | 4  | 3 |
|   M33  | Number createNumber(String str) | 157 | 21 |
|   M34  | String escapeCsv(String input) | 3 | 1 |
|   M35  | Number createNumber(String str) | 153 | 16 |
|   M36  | void setTimeZone(TimeZone zone) | 3 | 1 |
|   M37  | Date parse(String source) | 3 | 1 |
|   M38  | String random(int count, int start, int end, <br/>boolean letters, boolean numbers) | 3 | 1 |
|   M39  | String random(int count, String chars) | 5 | 2 |
|   M40  | String escapeXml(String input) | 3 | 1 |
|   M41  | String translate(CharSequence input) | 12  | 4 |
|   M42  | boolean isSameLocalTime(Calendar cal1, Calendar cal2) | 12 | 4 |
|   M43  | Fraction getReducedFraction(int numerator, int denominator) | 25  | 3 |
|   M44  | FastDateFormat getInstance(String pattern, Locale locale) | 3 | 1 |
|   M45  | Number createNumber(String str) | 150 | 16 |
|   M46  | String translate(CharSequence input) | 12 | 5 |
|   M47  | static Class<?>[] toClass(Object[] array) | 11 | 0 |
|   M48  | String format(Calendar calendar) | 3 | 3 |
|   M49  | String replaceEach(String text, <br/>String[] searchList, String[] replacementList) | 3 | 1 |
|   M50  | String getShortClassName(Class<?> cls) | 6 | 2 |
|   M51  | String format (Object obj) | 3 | 4 |
|   M52  | NumberUtils() | 3 | 1 |
|   M53  | String abbreviate(String str, int lower, <br/>int upper, String appendToEnd) | 38 | 7 |
|   M54  | String escapeJava(String str) | 3 | 1 |
|   M55  | Number createNumber(String str) | 150 | 23 |
|   M56  | Fraction reduce() | 9 | 3 |
|   M57  | Date round(Date date, int field) | 8 | 5 |
|   M58  | Locale toLocale(String str) | 36 | 10 |
|   M59  | HashSet(Collection<? extends E> c) | 4 | 3 |
|   M60  | boolean isNumber(String str) | 94 | 2 |
|   M61  | StrBuilder appendFixedWidthPadLeft(int value, <br/>int width, char padChar) | 3 | 2 |
|   M62  | int indexOf(String str) | 3 | 1 |
|   M63  | int compareTo(Object other) | 12 | 10 |
|   M64  | String format(Date date) | 4 | 3 |
|   M65  | BigFraction(final double value, final int maxDenominator) | 3 | 1 |
|   M66  | int sample() | 3 | 2 |
|   M67  | Line revert() | 4 | 2 |
|   M68  | double getValue() | 2 | 0 |
|   M69  | MultivariateNormalDistribution(final double[] means, <br/>final double[][] covariances) | 6 | 2 |
|   M70  | double max(final double a, final double b) | 19 | 1 |
|   M71  | Dfp newDfp(final String s) | 2 | 1 |
|   M72  | RealVector subtract(RealVector v) | 10 | 9 |
|   M73  | Fraction(double value, double epsilon, int maxIterations) | 4 | 1 |
|   M74  | double percentageValue() | 3 | 2 |
|   M75  | double mannWhitneyUTest(final double[] x, final double[] y) | 14 | 3 |
|   M76  | int inverseCumulativeProbability(final double p) | 43 | 14 |
|   M77  | PointValuePair optimize(final LinearObjectiveFunction f,<br/>final Collection<LinearConstraint> constraints,<br/>final GoalType goalType, final boolean restrictToNonNegative) | 31 | 0 |
|   M78  | Iterator<Chromosome> iterator() | 3 | 1 |
|   M79  | evaluate(final double[] values, final double[] weights, <br/>final double mean, final int begin, final int length) | 12 | 4 |
|   M80  | RealPointValuePair optimize(final LinearObjectiveFunction f, <br/>final Collection <LinearConstraint> constraints, <br/>final GoalType goalType, final boolean restrictToNonNegative) | 16 | 1 |
|   M81  | double solve(int maxEval, FUNC f, double min, double max, double startValue) | 6  | 2 |
|   M82  | RealVector ebeMultiply(RealVector v) | 11 | 4 |
|   M83  | Complex add(Complex rhs) | 5 | 4 |
|   M84  | void addObservedPoint(double x, double y) | 3 | 1 |
|   M85  | float max(final float a, final float b) | 3 | 1 |
|   M86  | UnivariateRealPointValuePair[] getOptima() | 5 | 2 |
|   M87  | double nextAfter(double d, double direction) | 38 | 6 |
|   M88  | double[][] getCovariances() | 28 | 7 |
|   M89  | double integrate(final FirstOrderDifferentialEquations equations, <br/>final double t0, final double[] y0, final double t, final double[] y) | 158 | 45 |
|   M90  | double getPct(Comparable<?> v) | 6 | 2 |
|   M91  | EigenDecompositionImpl(final double[] main, double[] secondary,<br/>final double splitTolerance) | 18 | 3 |
|   M92  | RealVector subtract(RealVector v) | 12 | 4 |
|   M93  | void addValue(Object v) | 28 | 6 |
|   M94  | int compareTo(Fraction object) | 4 | 2 |
|   M95  | int gcd(int u, int v) | 49 | 2 |
|   M96  | void setDenominatorDegreesOfFreedom(double degreesOfFreedom) | 6 | 1 |
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
|   M118  | void tryFoldStringJoin(NodeTraversal t, Node n, <br/>Node left, Node right, Node parent) | 88 | 40 |
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
|   M135  | double inverseCumulativeProbability(final double p) | 51 | 12 |
|   M136  | String format(JSError error, boolean warning) | 45 | 22 |
|   M137  | void inlineAliases(GlobalNamespace namespace) | 36 | 7 |
|   M138  | boolean contains(char ch) | 8 | 0 |
|   M139  | boolean toBoolean(String str) | 51 | 24 |
|   M140  | String unescape(String str) | 60 | 14 |
|   M141  | double density(double x) | 11 | 4 |
|   M142  | FastDateFormat getInstance(String pattern, Locale locale) | 3 | 1 |
|   M143  | Predicate<Node>() | 29 | 6 |
|   M144  | void inferPropertyTypesToMatchConstraint<br/>(JSType type, JSType constraint) | 24 | 12 |
|   M145  | boolean mayThrowException(Node n) | 20 | 5 |
|   M146  | void declareNameInScope(FlowScope scope, Node node, JSType type) | 23 | 10 |
|   M147  | boolean isFoldableExpressBlock(Node n) | 19 | 3 |
|   M148  | String toStringHelper(boolean forAnnotations) | 43 | 14 |
|   M149  | CompilerOptions createOptions() | 56 | 17 |
|   M150  | String getLine(int lineNumber) | 41 | 5 |
|   M151  | String normalizeSourceName(String filename) | 10 | 2 |
|   M152  | boolean isInlinableObject(List<Reference> refs) | 85 | 17 |
|   M153  | Node tryFoldArrayJoin(Node n) | 109 | 47 |
|   M154  | String strEscape(String s, char quote, String doublequoteEscape, <br/>String singlequoteEscape, String backslashEscape, CharsetEncoder outputCharsetEncoder) | 69 | 11 |
|   M155  | Node tryFoldShift(Node n, Node left, Node right) | 61 | 12 |
|   M156  | void handleObjectLit(NodeTraversal t, Node n) | 23 | 13 |
|   M157  | Complex atan() | 7 | 7 |
|   M158  | List<Cluster<T>> cluster(final Collection<T> points, <br/>final int k, final int maxIterations) | 25 | 7 |
|   M159  | DateTimeZone forOffsetHoursMinutes <br/> (int hoursOffset, int minutesOffset) | 20 | 4 |
|   M160  | PeriodFormatter standard() | 22 | 12 |
|   M161  | void setTimeZone(TimeZone zone) | 3 | 1 |
|   M162  | Number createNumber(String str) | 150 | 23 |
|   M163  | String join(Object[] array, char separator, <br/>int startIndex, int endIndex) | 19 | 5 |
|   M164  | float toJavaVersionInt(String version) | 3 | 2 |
|   M165  | Number createNumber(String str) | 147  | 19 |
|   M166  | long getTime() | 11 | 2 |
|   M167  | double getBoundarySize() | 4 | 3 |
|   M168  | void checkTheoreticalMinCost(double rms) | 4 | 1 |
|   M169  | Complex tanh() | 10 | 6 |
|   M170  | Node inlineReturnValue(Node callNode, Node fnNode) | 31 | 11 |
|   M171  | Paint getPaint(double value) | 6 | 3 |
|   M172  | boolean equals(CharSequence cs1, CharSequence cs2) | 9 | 1 |
|   M173  | double pow(double x, double y) | 158 | 4 |
|   M174  | double getMean() | 3 | 1 |
|   M175  | double doOptimize() | 3 | 1 |
|   M176  | double solve(final UnivariateRealFunction f, final double min, <br/>final double max, final double initial) | 42 | 8 |
|   M177  | JSType getDeclaredType(String sourceName, JSDocInfo info, <br/>Node lValue, @Nullable Node rValue) | 50 | 22 |
|   M178  | String strEscape(String s, char quote, String doublequoteEscape, <br/>String singlequoteEscape, String backslashEscape, CharsetEncoder outputCharsetEncoder) | 70 | 21 |