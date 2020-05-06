// Michael Freeman

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.List;

import javax.swing.*;

public class cashRegister implements ActionListener {
    JFrame cashFrame;
    JPanel mainPanel;
    JButton logOn;
    JButton reg;

    public static void main(String[] args) {
        new cashRegister();

    }

    public cashRegister() {
        // This is the frame for the register
        JFrame cashFrame = new JFrame("Cash Register");
        cashFrame.setLayout(new FlowLayout());
        cashFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);


        JPanel mainPanel = (JPanel)cashFrame.getContentPane();
        mainPanel.setLayout(new BoxLayout(mainPanel,BoxLayout.Y_AXIS));
        mainPanel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));

        // The welcome message!
        JPanel welcome = new JPanel();
        JLabel hello = new JLabel("Welcome to the system!");
        welcome.add(hello);
        mainPanel.add(welcome);

        // Button placements
        JPanel logButtons = new JPanel();
        logOn = new JButton("Log On");
        logOn.addActionListener(this);
        logButtons.add(logOn);
        reg = new JButton("Register");
        reg.addActionListener(this);
        logButtons.add(reg);
        mainPanel.add(logButtons);

        // Adjusts GUI size with contents and sets the entire GUI the be visible.
        cashFrame.pack();
        cashFrame.setVisible(true);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        Object control = e.getSource();
        if (control == reg) {
            new logR();
        }
    }
}
