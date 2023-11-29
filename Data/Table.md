
## Selected Real-world Faulty Methods
|   ID   |      Method Signature     |  Size(LOC)   | # Invoked Methods  |
|:------:|:----------------------------:|:-------:|:-------:|
|   M1   | int getItemCount() | 3 | 1 |
|   M2   | double getLowerBound() | 3 | 0 |
|   M3   | void setMaximumItemAge(long periods) | 7 | 2 |
|   M4   | Number getY(int index) | 3 | 1 |
|   M5   | int getMaxMiddleIndex() | 3 | 0 |
|   M6   | TimeSeries createCopy(RegularTimePeriod start, <br/>RegularTimePeriod end) | 38 | 4 |
|   M7   | String generateToolTipFragment(String toolTipText) | 4 | 0 |
|   M8   | Size2D arrange(Graphics2D g2, <br/>RectangleConstraint constraint) | 3 | 1 |
|   M9   | int getCategoryIndex(Comparable category) | 10 | 1 |
|   M10  | void addValue(double value, Comparable rowKey, <br/>Comparable columnKey) | 4 | 1 |
|   M11  | Paint getOutlinePaint() | 3 | 3 |
|   M12  | Range getRangeBounds(boolean includeInterval) | 3 | 0 |
|   M13  | void removeColumn(Comparable columnKey) | 12 | 6 |
|   M14  | void setDrawLines(boolean draw) | 5 | 2 |
|   M15  | void addYears(int) | 5  | 4 |
|   M16  | void addMonths(int) | 5  | 4 |
|   M17  | void addWeeks(int) | 5  | 4 |
|   M18  | void addDays(int) | 5  | 4 |
|   M19  | int get(DateTimeFieldType type) | 3 | 2 |
|   M20  | LocalDate addToCopy(int value) | 3 | 3 |
|   M21  | int parseInto(ReadWritableInstant instant, <br/>String text, int position) | 28 | 14 |
|   M22  | int mutableDateTime(ReadWritableInstant instant, <br/>String text, int position) | 28  | 14 |
|   M23  | DateTimeZone forOffsetHoursMinutes <br/> (int hoursOffset, int minutesOffset) | 23 | 3 |
|   M24  | DateTimeZone forOffsetHoursMinutes <br/> (int hoursOffset, int minutesOffset) | 20 | 4 |
|   M25  | Days daysBetween(ReadablePartial start, <br/>ReadablePartial end) | 10 | 7 |
|   M26  | LocalDateTime fromDateFields(Date date) | 14 | 9 |
|   M27  | PeriodFormatter standard() | 22 | 12 |
|   M28  | MonthDay minusMonths(int) | 9 | 6 |
|   M29  | MonthDay plusMonths(int) | 9 | 6 |
|   M30  | long safeMultiply(long val1, int val2) | 14 | 1 |
|   M31  | DateTime withLaterOffsetAtOverlap() | 4 | 4 |
|   M32  | int getDayOfMonth() | 3 | 4 |
|   M33  | Period toPeriod() | 3 | 2 |
|   M34  | LocalDate parseLocalDate(String text) | 3  | 2 |
|   M35  | DateTime withSecondOfMinute(int second) | 3 | 5 |
|   M36  | Period parsePeriod(String text) | 4  | 3 |
|   M37  | Number createNumber(String str) | 157 | 21 |
|   M38  | String escapeCsv(String input) | 3 | 1 |
|   M39  | Number createNumber(String str) | 153 | 16 |
|   M40  | void setTimeZone(TimeZone zone) | 3 | 1 |
|   M41  | Date parse(String source) | 3 | 1 |
|   M42  | void setTimeZone(TimeZone zone) | 3 | 1 |
|   M43  | String random(int count, int start, int end, <br/>boolean letters, boolean numbers) | 3 | 1 |
|   M44  | String random(int count, String chars) | 5 | 2 |
|   M45  | Number createNumber(String str) | 150 | 23 |
|   M46  | String escapeXml(String input) | 3 | 1 |
|   M47  | String translate(CharSequence input) | 12  | 4 |
|   M48  | String join(Object[] array, char separator, <br/>int startIndex, int endIndex) | 19 | 5 |
|   M49  | boolean isSameLocalTime(Calendar cal1, Calendar cal2) | 12 | 4 |
|   M50  | Fraction getReducedFraction(int numerator, int denominator) | 25  | 3 |
|   M51  | boolean isNumber(String str) | 102 | 2 |
|   M52  | FastDateFormat getInstance(String pattern, Locale locale) | 3 | 1 |
|   M53  | Number createNumber(String str) | 150 | 16 |
|   M54  | String translate(CharSequence input) | 12 | 5 |
|   M55  | float toJavaVersionInt(String version) | 3 | 2 |
|   M56  | static Class<?>[] toClass(Object[] array) | 11 | 0 |
|   M57  | Number createNumber(String str) | 147  | 19 |
|   M58  | String format(Calendar calendar) | 3 | 3 |
|   M59  | String replaceEach(String text, <br/>String[] searchList, String[] replacementList) | 3 | 1 |
|   M60  | String getShortClassName(Class<?> cls) | 6 | 2 |
|   M61  | String format (Object obj) | 3 | 4 |
|   M62  | NumberUtils() | 3 | 1 |
|   M63  | String abbreviate(String str, int lower, <br/>int upper, String appendToEnd) | 38 | 7 |
|   M64  | String escapeJava(String str) | 3 | 1 |
|   M65  | Number createNumber(String str) | 150 | 23 |
|   M66  | Fraction reduce() | 9 | 3 |
|   M67  | FastDateFormat getInstance(String pattern, Locale locale) | 3 | 1 |
|   M68  | boolean toBoolean(String str) | 51 | 24 |
|   M69  | String escapeJavaScript(String str) | 3 | 1 |
|   M70  | Date round(Date date, int field) | 8 | 5 |
|   M71  | Locale toLocale(String str) | 36 | 10 |
|   M72  | long getTime() | 11 | 2 |
|   M73  | HashSet(Collection<? extends E> c) | 4 | 3 |
|   M74  | boolean isNumber(String str) | 94 | 2 |
|   M75  | StrBuilder appendFixedWidthPadLeft(int value, <br/>int width, char padChar) | 3 | 2 |
|   M76  | boolean contains(char ch) | 8 | 0 |
|   M77  | int indexOf(String str) | 3 | 1 |
|   M78  | String unescape(String str) | 60 | 14 |
|   M79  | int compareTo(Object other) | 12 | 10 |
|   M80  | String format(Date date) | 4 | 3 |
|   M81  | BigFraction(final double value, final int maxDenominator) | 3 | 1 |
|   M82  | int sample() | 3 | 2 |
|   M83  | Line revert() | 4 | 2 |
|   M84  | double getValue() | 2 | 0 |
|   M85  | MultivariateNormalDistribution(final double[] means, <br/>final double[][] covariances) | 6 | 2 |
|   M86  | double max(final double a, final double b) | 19 | 1 |
|   M87  | Dfp newDfp(final String s) | 2 | 1 |
|   M88  | RealVector subtract(RealVector v) | 10 | 9 |
|   M89  | double density(double x) | 11 | 4 |
|   M90  | Fraction(double value, double epsilon, int maxIterations) | 4 | 1 |
|   M91  | double percentageValue() | 3 | 2 |
|   M92  | double mannWhitneyUTest(final double[] x, final double[] y) | 14 | 3 |
|   M93  | int inverseCumulativeProbability(final double p) | 43 | 14 |
|   M94  | double getBoundarySize() | 4 | 3 |
|   M95  | PointValuePair optimize(final LinearObjectiveFunction f,
                                       <br/>final Collection<LinearConstraint> constraints,
                                       <br/>final GoalType goalType, final boolean restrictToNonNegative) | 31 | 0 |
|   M96  | Iterator<Chromosome> iterator() | 3 | 1 |
|   M97  | evaluate(final double[] values, final double[] weights,
                           <br/>final double mean, final int begin, final int length) | 12  | 4 |
|   M98  | RealPointValuePair optimize(final LinearObjectiveFunction f,
                                       <br/>final Collection <LinearConstraint> constraints,
                                       <br/>final GoalType goalType, final boolean restrictToNonNegative) | 16 | 1 |
|   M99  | Complex atan() | 7 | 7 |
|   M100  | double solve(int maxEval, FUNC f, double min, double max, double startValue) | 6  | 2 |
|   M101  | RealVector ebeMultiply(RealVector v) | 11 | 4 |
|   M102  | Complex add(Complex rhs) | 5 | 4 |
|   M103  | void addObservedPoint(double x, double y) | 3 | 1 |
|   M104  | float max(final float a, final float b) | 3 | 1 |
|   M105  | UnivariateRealPointValuePair[] getOptima() | 5 | 2 |
|   M106  | double nextAfter(double d, double direction) | 38 | 6 |
|   M107  | void checkTheoreticalMinCost(double rms) | 4 | 1 |
|   M108  | double[][] getCovariances() | 28 | 7 |
|   M109  | double integrate(final FirstOrderDifferentialEquations equations,
                            <br/>final double t0, final double[] y0,
                            <br/>final double t, final double[] y) | 158 | 45 |
|   M110  | double getPct(Comparable<?> v) | 6 | 2 |
|   M111  | List<Cluster<T>> cluster(final Collection<T> points,
                                    <br/>final int k, final int maxIterations) | 25 | 7 |
|   M112  | EigenDecompositionImpl(final double[] main, double[] secondary,<br/>final double splitTolerance) | 18 | 3 |
|   M113  | RealVector subtract(RealVector v) | 12 | 4 |
|   M114  | double inverseCumulativeProbability(final double p) | 51 | 12 |
|   M115  | double[] getPoint() | 3 | 1 |
|   M116  | void addValue(Object v) | 28 | 6 |
|   M117  | int compareTo(Fraction object) | 4 | 2 |
|   M118  | int gcd(int u, int v) | 49 | 2 |
|   M119  | void setDenominatorDegreesOfFreedom(double degreesOfFreedom) | 6 | 1 |
|   M120  | Complex tanh() | 10 | 6 |
|   M121  | double solve(double min, double max) | 79 | 8 |
|   M122  | double doubleValue() | 26 | 3 |
|   M123  | double getSumSquaredErrors() | 3 | 0 |
|   M124  | Fraction parse(String source) | 8 | 4 |
|   M125  | void removeUnreferencedFunctionArgs(Scope fnScope) | 29 | 9 |
|   M126  | String normalizeSourceName(String filename) | 10 | 2 |
|   M127  | Predicate<Node>() | 29 | 6 |
|   M128  | void declareNameInScope(FlowScope scope, Node node, JSType type) | 23 | 10 |
|   M129  | Node tryFoldSimpleFunctionCall(Node n) | 22 | 14 |
|   M130  | Node tryFoldArrayAccess(Node n, Node left, Node right) | 50 | 11 |
|   M131  | void emitOptionalModuleExportsOverride(Node script, String moduleName) | 10 | 10 |
|   M132  | Node tryFinally(Node tryBody, Node finallyBody) | 5 | 6 |
|   M133  | void addIdentifier(String identifier) | 3 | 1 |
|   M134  | boolean isInlinableObject(List<Reference> refs) | 85 | 17 |
|   M135  | void inferPropertyTypesToMatchConstraint<br/>(JSType type, JSType constraint) | 24 | 12 |
|   M136  | void traverseFunction(Node n, Node parent) | 35 | 13 |
|   M137  | String toStringHelper(boolean forAnnotations) | 43 | 14 |
|   M138  | void visit(NodeTraversal t, Node n, Node parent) | 42 | 22 |
|   M139  | FunctionTypeBuilder inferFromOverriddenFunction(
      @Nullable FunctionType oldType, @Nullable Node paramsParent) | 54 | 21 |
|   M140  | void add(String newcode) | 21 | 5 |
|   M141  | Node tryFoldArrayJoin(Node n) | 109 | 47 |
|   M142  | String getLine(int lineNumber) | 41 | 5 |
|   M143  | String extractClassNameIfGoog(Node node, Node parent, String functionName) | 16 | 7 |
|   M144  | computeGenKill(Node n, BitSet gen, BitSet kill, boolean conditional) | 85 | 35 |
|   M145  | String format(JSError error, boolean warning) | 45 | 22 |
|   M146  | boolean isPrototypePropertyAssign(Node assign) | 20 | 11 |
|   M147  | Node parseBasicTypeExpression(JsDocToken token) | 25 | 19 |
|   M148  | void checkPropertyVisibility(NodeTraversal t, Node getprop, Node parent) | 93 | 26 |
|   M149  | String strEscape(String s, char quote,
                          <br/>String doublequoteEscape,
                          <br/>String singlequoteEscape,
                          <br/>String backslashEscape,
                          <br/>CharsetEncoder outputCharsetEncoder) | 69 | 11 |
|   M150  | int parseArguments(Parameters params) | 19  | 7 |
|   M151  | Node tryRemoveUnconditionalBranching(Node n) | 62 | 22 |
|   M152  | boolean isFoldableExpressBlock(Node n) | 19 | 3 |
|   M153  | VariableLiveness isVariableReadBeforeKill(Node n, String variable) | 11 | 4 |
|   M154  | boolean shouldTraverse(NodeTraversal t, Node n, Node parent) | 64 | 20 |
|   M155  | Node tryFoldShift(Node n, Node left, Node right) | 61 | 12 |
|   M156  | boolean mayThrowException(Node n) | 20 | 5 |
|   M157  | void tryFoldStringJoin(NodeTraversal t, Node n, <br/>Node left, Node right, Node parent) | 88 | 40 |
|   M158  | CompilerOptions createOptions() | 56 | 17 |
|   M159  | void exitScope(NodeTraversal t) | 13 | 5 |
|   M160  | Node parseContextTypeExpression(JsDocToken token) | 3 | 1 |
|   M161  | boolean inferTemplatedTypesForCall(<br/>Node n, FunctionType fnType) | 27 | 11 |
|   M162  | void recordAssignment(NodeTraversal t, Node n, Node recordNode) | 30 | 9 |
|   M163  | Node inlineReturnValue(Node callNode, Node fnNode) | 31 | 11 |
|   M164  | Node inlineReturnValue(Node callNode, Node fnNode) | 31 | 15 |
|   M165  | String getReadableJSTypeName(Node n, boolean dereference) | 53 | 24 |
|   M166  | void handleObjectLit(NodeTraversal t, Node n) | 23 | 13 |
|   M167  | void visitNew(NodeTraversal t, Node n) | 15 | 11 |
|   M168  | void tryMinimizeExits(Node n, int exitType, String labelName) | 95 | 33 |
|   M169  | void inlineAliases(GlobalNamespace namespace) | 36 | 7 |
|   M170  | String getRemainingJSDocLine() | 4 | 1 |
|   M171  | Paint getPaint(double value) | 6 | 3 |
|   M172  | boolean equals(CharSequence cs1, CharSequence cs2) | 9 | 1 |
|   M173  | double pow(double x, double y) | 158 | 4 |
|   M174  | double getMean() | 3 | 1 |
|   M175  | double doOptimize() | 3 | 1 |
|   M176  | double solve(final UnivariateRealFunction f, final double min, final double max, final double initial) | 42 | 8 |
|   M177  | JSType getDeclaredType(String sourceName, JSDocInfo info, <br/>Node lValue, @Nullable Node rValue) | 50 | 22 |
|   M178  | String strEscape(String s, char quote,
                          <br/>String doublequoteEscape,
                          <br/>String singlequoteEscape,
                          <br/>String backslashEscape,
                          <br/>CharsetEncoder outputCharsetEncoder) | 70 | 21 |
