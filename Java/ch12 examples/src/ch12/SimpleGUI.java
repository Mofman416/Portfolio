package ch12;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class SimpleGUI implements ActionListener{
	JFrame myFrame;
	JButton myButton1;
	JButton myButton2;
	
	public static void main(String[] args) {
		new SimpleGUI();
	}

	public SimpleGUI() {
	   myFrame = new JFrame();        // create the JFrame window
	   myFrame.setLayout(new FlowLayout());  // attach manager 
	   myFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

	   myButton1 = new JButton("Button 1"); 
	   myButton1.addActionListener(this);
	   myFrame.add(myButton1);     // add JButton to JFrame
	   myButton2 = new JButton("Button 2"); 
	   myButton2.addActionListener(this);
	   myFrame.add(myButton2);

	   myFrame.pack();
	   myFrame.setVisible(true); 
	}

	@Override
	public void actionPerformed(ActionEvent event) {
		Object control = event.getSource();
		   if (control == myButton1)  // if myButton1 was clicked
		   {
		      JOptionPane.showMessageDialog(myFrame,"I like Red!");
		   }
		   else if (control == myButton2)  // else if myButton2 was clicked
		   {
		      JOptionPane.showMessageDialog(myFrame,"I like Blue!");
		   }
		
	}

}
