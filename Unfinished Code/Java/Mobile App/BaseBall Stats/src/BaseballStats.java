//Michael Freeman
//Mobile App Development

import java.text.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.List;
import javax.swing.BorderFactory;
import javax.swing.BoxLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextField;
import javax.swing.JSpinner;
import javax.swing.JTextArea;
import javax.swing.SpinnerNumberModel;
import java.util.ArrayList;

public class BaseballStats implements ActionListener {

	DecimalFormat df;
	JFrame baseFrame;
	JPanel mainPanel;
	JTextField pname;
	JSpinner Game1Spinner;
	JSpinner Game2Spinner;
	JSpinner Game3Spinner;
	JSpinner Game4Spinner;
	JSpinner Game5Spinner;
	JTextArea players;
	JButton add;
	JButton reset;
	JButton show;
	ArrayList<Player> playerList = new ArrayList<Player>();
	
	public static void main(String[] args) {
		//This calls the program.
		new BaseballStats();

	}
	
	public BaseballStats() {
		//This defines the decimal format
		df = new DecimalFormat("0.000");
		
		//Main Frame
		JFrame baseFrame = new JFrame("Baseball Stats");
		baseFrame.setLayout(new FlowLayout());
		baseFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		JPanel mainPanel = (JPanel)baseFrame.getContentPane();
		mainPanel.setLayout(new BoxLayout(mainPanel,BoxLayout.Y_AXIS));
		mainPanel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
		
		//Player Input field
		JPanel tfield = new JPanel();
		JLabel name1 = new JLabel("Player Name:");
		tfield.add(name1);
		pname = new JTextField(20);
		tfield.add(pname);
		mainPanel.add(tfield);
		
		//Spinner Number Field - Game 1
		JPanel hitspin1 = new JPanel();
		JLabel game1 = new JLabel("Game 1 Hits:");
		hitspin1.add(game1);
		Game1Spinner = new JSpinner(new SpinnerNumberModel(0,0,5,1));
		hitspin1.add(Game1Spinner);
		mainPanel.add(hitspin1);
		
		//Spinner Number Field - Game 2
		JPanel hitspin2 = new JPanel();
		JLabel game2 = new JLabel("Game 2 Hits:");
		hitspin2.add(game2);
		Game2Spinner = new JSpinner(new SpinnerNumberModel(0,0,5,1));
		hitspin2.add(Game2Spinner);
		mainPanel.add(hitspin2);
		
		//Spinner Number Field - Game 3
		JPanel hitspin3 = new JPanel();
		JLabel game3 = new JLabel("Game 3 Hits:");
		hitspin3.add(game3);
		Game3Spinner = new JSpinner(new SpinnerNumberModel(0,0,5,1));
		hitspin3.add(Game3Spinner);
		mainPanel.add(hitspin3);
		
		//Spinner Number Field - Game 4
		JPanel hitspin4 = new JPanel();
		JLabel game4 = new JLabel("Game 4 Hits:");
		hitspin4.add(game4);
		Game4Spinner = new JSpinner(new SpinnerNumberModel(0,0,5,1));
		hitspin4.add(Game4Spinner);
		mainPanel.add(hitspin4);
		
		//Spinner Number Field - Game 5
		JPanel hitspin5 = new JPanel();
		JLabel game5 = new JLabel("Game 5 Hits:");
		hitspin5.add(game5);
		Game5Spinner = new JSpinner(new SpinnerNumberModel(0,0,5,1));
		hitspin5.add(Game5Spinner);
		mainPanel.add(hitspin5);
		
		//Displays list of players in an uneditable box.
		JPanel playList = new JPanel();
		JLabel playBox = new JLabel("Current Players:");
		playList.add(playBox);
		players = new JTextArea(5,20);
		players.setEditable(false);
		JScrollPane playScroll = new JScrollPane(players,
				JScrollPane.VERTICAL_SCROLLBAR_ALWAYS,
				JScrollPane.HORIZONTAL_SCROLLBAR_NEVER);
		playList.add(playScroll);
		mainPanel.add(playList);
		
		//Sets up the Add Player, Reset Values and Show Stats buttons.
		JPanel conResShow = new JPanel();
		add = new JButton("Add Player");
		add.addActionListener(this);
		conResShow.add(add);
		reset = new JButton("Reset Values");
		reset.addActionListener(this);
		conResShow.add(reset);
		show = new JButton("Show Stats");
		show.addActionListener(this);
		conResShow.add(show);
		mainPanel.add(conResShow);
		
		baseFrame.pack();
		baseFrame.setVisible(true);
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		//This tells the program what to do with the values.
		Object control = e.getSource();
		if (control == add) {
			String player = pname.getName();
		}
		
	}

}
