package ������Ϣ����;

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
	            while((line=bufrd.readLine())!=null) { //��ȡһ���ַ����������ַ���������������null
	            	if(flag == true) {
	            		String[] content = line.split(";");
	            		int len = content.length;
	            		
	            		tablemodel.addColumn("���");
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
	        catch(FileNotFoundException ex)                    //���ļ������ڣ�������ļ�
	        {
	            if(!file.getName().equals(""))
	        	    JOptionPane.showMessageDialog(null, "\""+file.getName()+"\"�ļ������ڡ�");
	        }
	        catch(IOException ex)
	        {
	            JOptionPane.showMessageDialog(null, "��ȡ�ļ�ʱ���ݴ���");
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
            while((line=bufrd.readLine())!=null) { //��ȡһ���ַ����������ַ���������������null
            	if(flag == true) {
            		String[] content = line.split(";");
            		int len = content.length;
            		tablemodel.addColumn("���");
            		for(int i = 0; i < len; i++)
            			tablemodel.addColumn(content[i]);
            		flag = false;
            	}else {
            		String[] content = line.split(";");
            		String regEx="[^0-9\\.]";  
            		Pattern p = Pattern.compile(regEx);  
            		Matcher m = p.matcher(content[Integer.valueOf(conditionIndex)-1]);  
            		content[Integer.valueOf(conditionIndex)-1] = m.replaceAll("").trim();
            		if(method.equals("����")) {
            			if(Float.valueOf(content[Integer.valueOf(conditionIndex)-1]) <= Float.valueOf(condition)) 
            				continue;           			           				
            		}
            		else if(method.equals("����")) {
            			if(Float.valueOf(content[Integer.valueOf(conditionIndex)-1]) != Float.valueOf(condition))
            				continue;			
            		}
            		else if(method.equals("С��")) {
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
        catch(FileNotFoundException ex)                    //���ļ������ڣ�������ļ�
        {
            if(!file.getName().equals(""))
        	    JOptionPane.showMessageDialog(null, "\""+file.getName()+"\"�ļ������ڡ�");
//            JOptionPane.showMessageDialog(null, "\""+file.getAbsolutePath()+"\"�ļ������ڡ�");
        }
        catch(IOException ex)
        {
            JOptionPane.showMessageDialog(null, "��ȡ�ļ�ʱ���ݴ���");
        }
    }
}
