// File used to register within the Register system

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.List;

import javax.swing.*;

public class logR implements ActionListener{
    JFrame regFrame;
    JPanel mainPanel;

    public logR() {
        JFrame regFrame = new JFrame("Register New Employee");
        regFrame.setLayout(new FlowLayout());

        JPanel mainPanel = (JPanel)regFrame.getContentPane();
        mainPanel.setLayout(new BoxLayout(mainPanel,BoxLayout.Y_AXIS));
        mainPanel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));

        // Adjusts GUI size with contents and sets the entire GUI the be visible.
        regFrame.pack();
        regFrame.setVisible(true);
    }

    @Override
    public void actionPerformed(ActionEvent e) {

    }
}
