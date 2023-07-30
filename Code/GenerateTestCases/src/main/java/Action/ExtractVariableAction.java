//package Action;
//
//import MyUtils.Editors;
//import MyUtils.ExtractVariable;
//import MyUtils.MethodExtractor;
//import com.github.javaparser.StaticJavaParser;
//import com.github.javaparser.ast.body.MethodDeclaration;
//import com.github.javaparser.ast.expr.*;
//import com.github.javaparser.ast.stmt.BlockStmt;
//import com.intellij.openapi.actionSystem.AnAction;
//import com.intellij.openapi.actionSystem.AnActionEvent;
//import com.intellij.openapi.actionSystem.CommonDataKeys;
//import com.intellij.openapi.editor.CaretModel;
//import com.intellij.openapi.editor.Document;
//import com.intellij.openapi.editor.Editor;
//import com.intellij.openapi.fileEditor.FileDocumentManager;
//import com.intellij.openapi.project.Project;
//import com.intellij.openapi.ui.Messages;
//import com.intellij.openapi.vfs.VirtualFile;
//import org.jetbrains.annotations.NotNull;
//
//import java.util.ArrayList;
//
//import org.junit.Assert;
//
//import java.io.*;
//import java.util.List;
//
//public class ExtractVariableAction extends AnAction {
//    // 具有偏移量和参数的自定义对象
//    class OffsetArgument {
//        private int offset;
//        private String argument;
//
//        public OffsetArgument(int offset, String argument) {
//            this.offset = offset;
//            this.argument = argument;
//        }
//
//        public int getOffset() {
//            return offset;
//        }
//
//        public String getArgument() {
//            return argument;
//        }
//    }
//
//    public void actionPerformed(@NotNull AnActionEvent e) {
//        final Editor editor = e.getData(CommonDataKeys.EDITOR);
//        Project project = e.getProject();
////        CaretModel caretModel = editor.getCaretModel();
////        int caretModelOffset = caretModel.getOffset();
////        int lineStartOffset = editor.getDocument().getLineStartOffset(caretModel.getLogicalPosition().line);
////        int columnOffset = caretModelOffset - lineStartOffset;
////        Messages.showMessageDialog(project, "editorOffset:" + caretModelOffset, "columnOffset:" + columnOffset, Messages.getInformationIcon());
//        String absoluteJavaFilePath = getAbsoluteFilePath(editor);
//        Document document = Editors.getCurrentDocument(absoluteJavaFilePath);
//        String selectedText = editor.getSelectionModel().getSelectedText();
//        if (selectedText == null || selectedText.isEmpty()) {
//            return;
//        }
//        String methodBody = null;
//        try {
//            methodBody = String.valueOf(MethodExtractor.parseSelectedMethod(editor.getDocument().getText(), selectedText));
//        } catch (IOException ex) {
//            throw new RuntimeException(ex);
//        }
//        if (methodBody == null) {
//            return;
//        }
//        // Find assert statements in the method body
//        MethodDeclaration methodDeclaration = StaticJavaParser.parseMethodDeclaration(methodBody);
//        BlockStmt methods = methodDeclaration.getBody().get();
//        List<MethodCallExpr> methodCalls = methods.findAll(MethodCallExpr.class);
//        MethodExtractor methodExtractor = new MethodExtractor();
//
//        // 获取选中方法的起始行号和结束行号
//        int selectedMethodStartLine = methodExtractor.getStartLine();
//        List<OffsetArgument> offsets = new ArrayList<>();
//
//        for (MethodCallExpr methodCall : methodCalls) {
//            String methodName = methodCall.getNameAsString();
//            if (methodName.equals("assertEquals") || methodName.equals("Assert.assertEquals") || methodName.equals("assertFalse") || methodName.equals("assertTrue")) {
//                List<Expression> arguments = methodCall.getArguments();
//                for (Expression argument : arguments) {
//                    // 判断表达式类型
//                    if (argument instanceof LiteralExpr || argument instanceof NameExpr || (argument instanceof UnaryExpr && ((UnaryExpr) argument).getOperator() == UnaryExpr.Operator.MINUS)) {
//                        // 忽略字面量表达式、变量名表达式和负数表达式
//                        continue;
//                    }
//                    // 判断是否在选中方法范围内
//                    int expressionStartLine = argument.getBegin().get().line - 1;
//                    int expressionColumn = argument.getBegin().get().column + 3;
//                    expressionStartLine = expressionStartLine + selectedMethodStartLine;
////                    Messages.showMessageDialog(project, "expressionStartLine:" + expressionStartLine, "expressionColumn:" + expressionColumn, Messages.getInformationIcon());
//                    int offset = getOffset(absoluteJavaFilePath, expressionStartLine, expressionColumn);
//                    String argumentString = argument.toString();
//                    offsets.add(new OffsetArgument(offset, argumentString));
////                    Messages.showMessageDialog(project, "offset:" + offset, argument.toString(), Messages.getInformationIcon());
//                    // 根据偏移量进行操作
//                }
//            }
//        }
//        // Process each offset using the stored offsets
//        for (OffsetArgument offsetArgument : offsets) {
//            int offset = offsetArgument.getOffset();
//            String argument = offsetArgument.getArgument();
//            idea_parseEachJavaFileOfSpecificCommit(document, project, absoluteJavaFilePath, offset, argument);
//        }
//        // 将替换后的文本写入文件
//        writeToFile(absoluteJavaFilePath, document.getText());
//    }
//
//    public static int getOffset(String filePath, int lineOffset, int columnOffset) {
//        try {
//            File file = new File(filePath);
//            BufferedReader reader = new BufferedReader(new FileReader(file));
//            StringBuilder fileContent = new StringBuilder();
//            String line;
//            int currentOffset = 0;
//            int currentLine = 0;
//
//            while ((line = reader.readLine()) != null) {
//                fileContent.append(line).append(System.lineSeparator());
//
//                currentLine++;
//                if (currentLine == lineOffset) {
//                    int index = columnOffset;
//                    if (index <= line.length()) {
//                        // Found the target position in the current line
//                        return currentOffset + index;
//                    }
//                    break;
//                }
//                currentOffset += line.length() + System.lineSeparator().length();
//            }
//            reader.close();
//
//            // The target position was not found
//            return -1;
//        } catch (IOException e) {
//            e.printStackTrace();
//            return -1;
//        }
//    }
//
//    private String getAbsoluteFilePath(Editor editor) {
//        VirtualFile virtualFile = FileDocumentManager.getInstance().getFile(editor.getDocument());
//        if (virtualFile != null) {
//            return virtualFile.getPath();
//        }
//        return null;
//    }
//
//    private void idea_parseEachJavaFileOfSpecificCommit(Document document, Project project, String newFilePath, int offset, String expression) {
//        ExtractVariable extractVariable = new ExtractVariable(project, offset, newFilePath, expression);
//        extractVariable.extractVariable();
//    }
//
//    private void writeToFile(String filePath, String content) {
//        try {
//            BufferedWriter out = new BufferedWriter(new FileWriter(filePath));
//            out.write(content);
//            out.close();
//        } catch (IOException e) {
//            e.printStackTrace();
//        }
//    }
//}

package Action;

import MyUtils.Editors;
import MyUtils.ExtractVariable;
import MyUtils.MethodExtractor;
import com.github.javaparser.StaticJavaParser;
import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.ast.expr.*;
import com.github.javaparser.ast.stmt.BlockStmt;
import com.intellij.openapi.actionSystem.AnAction;
import com.intellij.openapi.actionSystem.AnActionEvent;
import com.intellij.openapi.actionSystem.CommonDataKeys;
import com.intellij.openapi.editor.Document;
import com.intellij.openapi.editor.Editor;
import com.intellij.openapi.fileEditor.FileDocumentManager;
import com.intellij.openapi.project.Project;
import com.intellij.openapi.ui.Messages;
import com.intellij.openapi.vfs.VirtualFile;
import org.jetbrains.annotations.NotNull;

import java.io.*;
import java.util.List;

public class ExtractVariableAction extends AnAction {
    public void actionPerformed(@NotNull AnActionEvent e) {
        final Editor editor = e.getData(CommonDataKeys.EDITOR);
        Project project = e.getProject();
        String absoluteJavaFilePath = getAbsoluteFilePath(editor);
        Document document = Editors.getCurrentDocument(absoluteJavaFilePath);
        String selectedText = editor.getSelectionModel().getSelectedText();
        if (selectedText == null || selectedText.isEmpty()) {
            return;
        }
        String methodBody = null;
        try {
            methodBody = String.valueOf(MethodExtractor.parseSelectedMethod(editor.getDocument().getText(), selectedText));
        } catch (IOException ex) {
            throw new RuntimeException(ex);
        }
        if (methodBody == null) {
            return;
        }
        // Find assert statements in the method body
        MethodDeclaration methodDeclaration = StaticJavaParser.parseMethodDeclaration(methodBody);
        BlockStmt methods = methodDeclaration.getBody().get();
        List<MethodCallExpr> methodCalls = methods.findAll(MethodCallExpr.class);
        MethodExtractor methodExtractor = new MethodExtractor();

        for (MethodCallExpr methodCall : methodCalls) {
            String methodName = methodCall.getNameAsString();
            if (methodName.equals("assertEquals") || methodName.equals("assertArrayEquals")) {
                List<Expression> arguments = methodCall.getArguments();
                for (Expression argument : arguments) {
                    // 判断表达式类型
                    if (argument instanceof LiteralExpr || argument instanceof NameExpr || (argument instanceof UnaryExpr && ((UnaryExpr) argument).getOperator() == UnaryExpr.Operator.MINUS)) {
                        // 忽略字面量表达式、变量名表达式和负数表达式
                        continue;
                    }
                    String expression = String.valueOf(argument);
                    int offset = getOffset(absoluteJavaFilePath, expression);
                    // 根据光标位置替换
//                    Messages.showMessageDialog(project, offset + " ",
//                            expression, Messages.getInformationIcon());
                    idea_parseEachJavaFileOfSpecificCommit(document, project, absoluteJavaFilePath, offset, expression);
                }
                // 将替换后的文本写入文件
                writeToFile(absoluteJavaFilePath, document.getText());
            }
        }
    }

    public static int getOffset(String filePath, String searchString) {
        try {
            File file = new File(filePath);
            BufferedReader reader = new BufferedReader(new FileReader(file));

            StringBuilder fileContent = new StringBuilder();
            String line;
            int currentOffset = 0;

            while ((line = reader.readLine()) != null) {
                fileContent.append(line).append(System.lineSeparator());

                int index = line.indexOf(searchString);
                if (index != -1) {
                    // Found the target string in the current line
                    return currentOffset + index;
                }
                currentOffset += line.length() + System.lineSeparator().length();
            }
            reader.close();

            // The target string was not found
            return -1;
        } catch (IOException e) {
            e.printStackTrace();
            return -1;
        }
    }

    private String getAbsoluteFilePath(Editor editor) {
        VirtualFile virtualFile = FileDocumentManager.getInstance().getFile(editor.getDocument());
        if (virtualFile != null) {
            return virtualFile.getPath();
        }
        return null;
    }

    private void idea_parseEachJavaFileOfSpecificCommit(Document document, Project project, String newFilePath, int offset, String expression) {
        if (document == null) return;
        ExtractVariable extractVariable = new ExtractVariable(project, offset, newFilePath, expression);
//        Messages.showMessageDialog(project, extractVariable.findPsiExpression(offset, expression).toString(),
//                "Introduce Variable", Messages.getInformationIcon());
        extractVariable.extractVariable();
    }

    private void writeToFile(String filePath, String content) {
        try {
            BufferedWriter out = new BufferedWriter(new FileWriter(filePath));
            out.write(content);
            out.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
