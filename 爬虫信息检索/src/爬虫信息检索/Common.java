package 爬虫信息检索;

import java.io.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import javax.swing.JOptionPane;
import javax.swing.table.DefaultTableModel;




public class Common {
		
	public static void ReadFrom(File file,DefaultTableModel tablemodel)
	    {	
			tablemodel.setRowCount(0);
			tablemodel.setColumnCount(0);
			boolean flag = true;
			int count = 0;
	        try
	        {
	        	BufferedReader bufrd = new BufferedReader(new InputStreamReader(new FileInputStream(file), "UTF-8"));            
	            String line;
	            while((line=bufrd.readLine())!=null) { //读取一行字符串，缓冲字符输入流结束返回null
	            	if(flag == true) {
	            		String[] content = line.split(";");
	            		int len = content.length;
	            		
	            		tablemodel.addColumn("序号");
	            		for(int i = 0; i < len; i++)
	            			tablemodel.addColumn(content[i]);
	            		flag = false;
	            	}else {
	            		String[] content = line.split(";");
	            		String[] count_add_content = new String[content.length+1];
	            		count++;
	            		count_add_content[0] = String.valueOf(count);
	            		for(int i = 0; i < content.length; i++)
	            			count_add_content[i+1] = content[i];
	            		tablemodel.addRow(count_add_content);
	            	}
	            	
	            	
	            }
	            bufrd.close();
	            
	        }
	        catch(FileNotFoundException ex)                    //若文件不存在，则忽略文件
	        {
	            if(!file.getName().equals(""))
	        	    JOptionPane.showMessageDialog(null, "\""+file.getName()+"\"文件不存在。");
	        }
	        catch(IOException ex)
	        {
	            JOptionPane.showMessageDialog(null, "读取文件时数据错误");
	        }
	    }
	
	public static void ReadSpeFrom(File file,DefaultTableModel tablemodel,String conditionIndex,String method,String condition)
    {	
		tablemodel.setRowCount(0);
		tablemodel.setColumnCount(0);
		boolean flag = true;
		int count = 0;
        try
        {
        	BufferedReader bufrd = new BufferedReader(new InputStreamReader(new FileInputStream(file), "UTF-8"));            
            String line;
            while((line=bufrd.readLine())!=null) { //读取一行字符串，缓冲字符输入流结束返回null
            	if(flag == true) {
            		String[] content = line.split(";");
            		int len = content.length;
            		tablemodel.addColumn("序号");
            		for(int i = 0; i < len; i++)
            			tablemodel.addColumn(content[i]);
            		flag = false;
            	}else {
            		String[] content = line.split(";");
            		String regEx="[^0-9\\.]";  
            		Pattern p = Pattern.compile(regEx);  
            		Matcher m = p.matcher(content[Integer.valueOf(conditionIndex)-1]);  
            		content[Integer.valueOf(conditionIndex)-1] = m.replaceAll("").trim();
            		if(method.equals("大于")) {
            			if(Float.valueOf(content[Integer.valueOf(conditionIndex)-1]) <= Float.valueOf(condition)) 
            				continue;           			           				
            		}
            		else if(method.equals("等于")) {
            			if(Float.valueOf(content[Integer.valueOf(conditionIndex)-1]) != Float.valueOf(condition))
            				continue;			
            		}
            		else if(method.equals("小于")) {
            			if(Float.valueOf(content[Integer.valueOf(conditionIndex)-1]) >= Float.valueOf(condition))
            				continue;          			
            		}         		
	            	String[] count_add_content = new String[content.length+1];
	            	count++;
	            	count_add_content[0] = String.valueOf(count);
	            	for(int i = 0; i < content.length; i++)
	            		count_add_content[i+1] = content[i];
	            	tablemodel.addRow(count_add_content);           		
            	}
            	
            	
            }
            bufrd.close();
        }
        catch(FileNotFoundException ex)                    //若文件不存在，则忽略文件
        {
            if(!file.getName().equals(""))
        	    JOptionPane.showMessageDialog(null, "\""+file.getName()+"\"文件不存在。");
//            JOptionPane.showMessageDialog(null, "\""+file.getAbsolutePath()+"\"文件不存在。");
        }
        catch(IOException ex)
        {
            JOptionPane.showMessageDialog(null, "读取文件时数据错误");
        }
    }
}
