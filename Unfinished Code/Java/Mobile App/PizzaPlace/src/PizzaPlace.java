import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.*;

public class PizzaPlace implements ActionListener {
	JFrame pizzaFrame;
	JPanel mainPanel;
	JTextField cname;
	JRadioButton pizzaSmall;
	JRadioButton pizzaMed;
	JRadioButton pizzaLarge;
	@SuppressWarnings("rawtypes")
	JComboBox crust;
	@SuppressWarnings("rawtypes")
	JList pTop;
	JCheckBox bread;
	JCheckBox salad;
	JCheckBox soda;
	JTextArea customer;
	JButton confirm;
	JButton reset;
	String size;
	
	
	public static void main(String[] args) {
		new PizzaPlace();

	}

	public PizzaPlace() {
		//The main pizza frame.
		JFrame pizzaFrame = new JFrame("Pizza Place");
		pizzaFrame.setLayout(new FlowLayout());
		pizzaFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		JPanel mainPanel = (JPanel)pizzaFrame.getContentPane();
		mainPanel.setLayout(new BoxLayout(mainPanel,BoxLayout.Y_AXIS));
		mainPanel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
		
		//Text field asking for the customer name.
		JPanel tfield = new JPanel();
		JLabel name1 = new JLabel("Custome Name:");
		tfield.add(name1);
		JTextField cname = new JTextField(20);
		tfield.add(cname);
		mainPanel.add(tfield);
		
		//Radio buttons asking for the pizza size.
		JPanel pbutton = new JPanel();
		JLabel name2 = new JLabel("Pizza Size:");
		pbutton.add(name2);
		JRadioButton pizzaSmall = new JRadioButton("Small");
		pizzaSmall.addActionListener(this);
		pbutton.add(pizzaSmall);
		JRadioButton pizzaMed = new JRadioButton("Medium");
		pizzaMed.addActionListener(this);
		pbutton.add(pizzaMed);
		JRadioButton pizzaLarge = new JRadioButton("Large");
		pizzaLarge.addActionListener(this);
		pbutton.add(pizzaLarge);
		ButtonGroup radioGroup = new ButtonGroup();
		radioGroup.add(pizzaSmall);
		radioGroup.add(pizzaMed);
		radioGroup.add(pizzaLarge);
		mainPanel.add(pbutton);
		
		//Combo box to select the crust type.
		JPanel cbox = new JPanel();
		JLabel name3 = new JLabel("Crust Type:");
		cbox.add(name3);
		String[] pizzaCrust = {"Thin", "Thick", "Deep Dish"};
		JComboBox crust = new JComboBox(pizzaCrust);
		cbox.add(crust);
		mainPanel.add(cbox);
		
		//This is a multi-list box for pizza toppings.
		JPanel topList = new JPanel();
		JLabel name4 = new JLabel("Toppings:");
		topList.add(name4);
		String[] toppings = {"Pepperoni", "Sausage", "Green Peppers",
				"Onions", "Tomatoes", "Anchovies", "Bacon", "Chicken",
				"Beef", "Olives", "Mushrooms", "Pineapple"};
		JList pTop = new JList(toppings);
		pTop.setSelectionMode(ListSelectionModel.MULTIPLE_INTERVAL_SELECTION);
		JScrollPane topScroll = new JScrollPane(pTop,
				JScrollPane.VERTICAL_SCROLLBAR_ALWAYS,
				JScrollPane.HORIZONTAL_SCROLLBAR_NEVER);
		topList.add(topScroll);
		mainPanel.add(topList);
		
		/*These are check boxes that are used for extra items to add
		to the order*/
		JPanel exItems = new JPanel();
		JLabel name5 = new JLabel("Extras:");
		exItems.add(name5);
		JCheckBox bread = new JCheckBox("Bread Sticks");
		bread.addActionListener(this);
		exItems.add(bread);
		JCheckBox salad = new JCheckBox("Salad");
		bread.addActionListener(this);
		exItems.add(salad);
		JCheckBox soda = new JCheckBox("Soda");
		soda.addActionListener(this);
		exItems.add(soda);
		mainPanel.add(exItems);
		
		//This is a text area to hold any customer comments.
		JPanel cusCom = new JPanel();
		JLabel name6 = new JLabel("Order Comments:");
		cusCom.add(name6);
		JTextArea customer = new JTextArea(5,20);
		JScrollPane cusScroll = new JScrollPane(customer,
				JScrollPane.VERTICAL_SCROLLBAR_ALWAYS,
				JScrollPane.HORIZONTAL_SCROLLBAR_NEVER);
		cusCom.add(cusScroll);
		mainPanel.add(cusCom);
		
		//This makes two buttons to confirm order or reset the fields.
		JPanel conRes = new JPanel();
		JButton confirm = new JButton("Place Order");
		confirm.addActionListener(this);
		conRes.add(confirm);
		JButton reset = new JButton("Reset Values");
		reset.addActionListener(this);
		conRes.add(reset);
		mainPanel.add(conRes);
		
		//Implements ActionListener to handle button clicks.
		
		
		
		
		
		
		
		
		
		pizzaFrame.pack();
		pizzaFrame.setVisible(true);
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		//This tells the program what to do and how to get values.
		Object control = e.getSource();
		if (control == confirm) {
			String customer = cname.getText();
			
			if (pizzaSmall.isSelected()) {
				size = "Small";
			}
			
			else if (pizzaMed.isSelected()) {
				size = "Medium";
			}
			
			else {
				size = "Large";
			}
			String size = pbutton.getSelectedItem();
			
			String
			
			
		}
		
	}

}
