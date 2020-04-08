package 爬虫信息检索;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import javax.swing.*;
import javax.swing.table.DefaultTableModel;



public class MainFrame extends JFrame implements ActionListener {
	private JPanel header;
	public DefaultTableModel tableModel;
	protected JFileChooser fchooser;
	private JComboBox<String> method;
	private JTextField firstText,secondText;
	private String[] methods = {"大于","等于","小于"};
	private String[] btns = {"检索","写入文件","还原"};
	protected DefaultComboBoxModel<String> model;
	private File file;
	
	public MainFrame() {
		super("信息检索");
		this.setBounds(300, 240, 800, 400);
		this.setDefaultCloseOperation(EXIT_ON_CLOSE);
		
		header = new JPanel();
		model = new DefaultComboBoxModel<String>();
		method = new JComboBox<String>(model);
		for(int i = 0; i < methods.length; i++)
			model.addElement(methods[i]);
		
		firstText = new JTextField("",8);
		secondText = new JTextField("",8);
		header.add(new JLabel("请输入要筛选的条件的索引(序号列为0):"));
		header.add(firstText);
		header.add(method);
		header.add(secondText);
		
		this.fchooser = new JFileChooser();
		
		
		for(int i = 0; i < btns.length; i++) {
			JButton button = new JButton(btns[i]);
			button.addActionListener(this);
			header.add(button);
		}
		header.setBackground(Color.LIGHT_GRAY);
		this.add(header,BorderLayout.NORTH);
		
		tableModel = new DefaultTableModel();
		JTable table = new JTable(tableModel);
		
		this.add(new JScrollPane(table));
		
		
		
		this.setVisible(true);
	}
	
	
	@Override
	public void actionPerformed(ActionEvent e) {
		// TODO Auto-generated method stub
		switch(e.getActionCommand()) {
			case "写入文件":
				if(fchooser.showOpenDialog(this) == JFileChooser.APPROVE_OPTION) {
					file = fchooser.getSelectedFile();
		 			Common.ReadFrom(file, tableModel);	 			
		 		}
				break;
			case "检索":
				if(file == null) {
					JOptionPane.showMessageDialog(null, "请先写入文件");
					break;
				}
				String firTextVal = firstText.getText().trim();
				String theMethod = method.getSelectedItem().toString();
				String secTextVal = secondText.getText().trim();
				String regEx="[^0-9\\.]";  
        		Pattern p = Pattern.compile(regEx);  
        		Matcher m = p.matcher(secTextVal);  
        		secTextVal = m.replaceAll("").trim();
        		
				if(firTextVal.equals("") || secTextVal.equals("")){
					JOptionPane.showMessageDialog(null, "条件不能为空");
					break;
				}
				Common.ReadSpeFrom(file, tableModel, firTextVal, theMethod, secTextVal);
				break;
			case "还原":
				if(file == null) {
					JOptionPane.showMessageDialog(null, "请先写入文件");
					break;
				}
					
				Common.ReadFrom(file, tableModel);	 
				
				break;
		}
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new MainFrame();
	}


}
