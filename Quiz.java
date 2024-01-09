package Quiz;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Quiz {

private JFrame frame;
private JPanel p1,p2,p3;
private JLabel [] arrayLabels;
private JRadioButton [] arrayRButtons;
private ButtonGroup[] arrayGroups;
private JPanel [] arrayPanels;
private CardLayout cl;
private JLabel lb1,lb2;
private JButton btn1,btn2;
private Timer tim;
private int t,s;

public Kviz(){
prepareGUI();
}

private void prepareGUI(){

frame=new JFrame();
frame.setSize(400, 400);
frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
frame.setLocationRelativeTo(null);
frame.setLayout(new BorderLayout());

p1=new JPanel();
p1.setLayout(new FlowLayout());

lb1=new JLabel("Wellcome to quiz");

cl=new CardLayout();

p2=new JPanel();
p2.setLayout(cl);

arrayPanels = new JPanel[10];

//A series of panels on which will rotate and show questions and answers
for(int i=0;i<arrayPanels.length;i++){

    arrayPanels[i] = new JPanel();
    p2.add(arrayPanels[i], String.valueOf(i));
    arrayPanels[i].setLayout(new GridLayout(0,1));

}

//Array RadioButtons with text

arrayRButtons = new JRadioButton[40];

for(int i=0;i<arrayRButtons.length;i++){
    arrayRButtons[i] = new JRadioButton();

    switch(i){
        case 0:arrayRButtons[i].setText("Mesopotamia");
            break;
        case 1:arrayRButtons[i].setText("Greece");
            break;
        case 2:arrayRButtons[i].setText("China");
            break;
        case 3:arrayRButtons[i].setText("Egypt");
            break;
        case 4:arrayRButtons[i].setText("Kinshasa");
            break;
        case 5:arrayRButtons[i].setText("Lagos");
            break;
        case 6:arrayRButtons[i].setText("Ulan Bator");
            break;
        case 7:arrayRButtons[i].setText("Abu Dhabi");
            break;
        case 8:arrayRButtons[i].setText("United Kingdom");
            break;
        case 9:arrayRButtons[i].setText("Norway");
            break;
        case 10:arrayRButtons[i].setText("USA");
            break;
        case 11:arrayRButtons[i].setText("Denmark");
            break;
        case 12:arrayRButtons[i].setText("Step mom");
            break;
        case 13:arrayRButtons[i].setText("Runaway Bride");
            break;
        case 14:arrayRButtons[i].setText("Grease");
            break;
        case 15:arrayRButtons[i].setText("Nothing Hill");
            break;
        case 16:arrayRButtons[i].setText("Neil Armstrong");
            break;
        case 17:arrayRButtons[i].setText("John Lenon");
            break;
        case 18:arrayRButtons[i].setText("Martin Luter King");
            break;
        case 19:arrayRButtons[i].setText("Winston Churchill");
            break;
        case 20:arrayRButtons[i].setText("Mecca");
            break;
        case 21:arrayRButtons[i].setText("Medina");
            break;
        case 22:arrayRButtons[i].setText("Dubai");
            break;
        case 23:arrayRButtons[i].setText("Riyadh");
            break;
        case 24:arrayRButtons[i].setText("Spain");
            break;
        case 25:arrayRButtons[i].setText("Venice");
            break;
        case 26:arrayRButtons[i].setText("Portugal");
            break;
        case 27:arrayRButtons[i].setText("Genoa");
            break;
        case 28:arrayRButtons[i].setText("Holocaust");
            break;
        case 29:arrayRButtons[i].setText("Perl Harbour");
            break;
        case 30:arrayRButtons[i].setText("The attack on France");
            break;
        case 31:arrayRButtons[i].setText("Blitzkrieg on Poland");
            break;
        case 32:arrayRButtons[i].setText("Bon");
            break;
        case 33:arrayRButtons[i].setText("Munich");
            break;
        case 34:arrayRButtons[i].setText("Leipzig");
            break;
        case 35:arrayRButtons[i].setText("Hamburg");
            break;
        case 36:arrayRButtons[i].setText("Chile");
            break;
        case 37:arrayRButtons[i].setText("East Timor");
            break;
        case 38:arrayRButtons[i].setText("Portugal");
            break;
        case 39:arrayRButtons[i].setText("Brazil");
            break;

    }
}

//Array button's grups 
arrayGroups=new ButtonGroup[10];

int j=0;
for(int i=0;i<arrayGroups.length;i++){

arrayGroups[i] = new ButtonGroup();

arrayGroups[i].add(arrayRButtons[j]);
arrayGroups[i].add(arrayRButtons[j+1]);
arrayGroups[i].add(arrayRButtons[j+2]);
arrayGroups[i].add(arrayRButtons[j+3]);

j+=4;
}

//Labels array with questions
arrayLabels = new JLabel[10];

for(int i=0;i<arrayLabels.length;i++){
    arrayLabels[i] = new JLabel();
    switch(i){
        case 0:arrayLabels[i].setText("The homeland of Olympics is");
            break;
        case 1:arrayLabels[i].setText("What is the capital of Nigeria");
            break;
        case 2:arrayLabels[i].setText("Which country have Greenland");
            break;
        case 3:arrayLabels[i].setText("In which the film except \"Pretty Women\" acters are Julia Roberts and Richard Gere");
            break;
        case 4:arrayLabels[i].setText("What is the first man on the moon?");
            break;
        case 5:arrayLabels[i].setText("The capital city of Saudi Arabia");
            break;
        case 6:arrayLabels[i].setText("Christopher Columbus come from ");
            break;
        case 7:arrayLabels[i].setText("Which the event stated the United States to engage in war");
            break;
        case 8:arrayLabels[i].setText("Which city was the capital in the unification of Germany");
            break;
        case 9:arrayLabels[i].setText("In which country dictator Salazar was in power ");
            break;
    }
}

p3=new JPanel();
p3.setLayout(new FlowLayout());

//Rotate panels with questions
btn1=new JButton("Next question");
btn1.setEnabled(false);
btn1.addActionListener(new ActionListener(){
    @Override
    public void actionPerformed(ActionEvent e){
        cl.next(p2);
        btn1.setEnabled(false);
        btn2.setEnabled(true);
        t=10;
        lb2.setText(String.valueOf(t));
        tim.start();
        btn1.setText("Next question");
    }
});


btn2=new JButton("Answer on question");
btn2.addActionListener(new ActionListener(){
    @Override
    public void actionPerformed(ActionEvent e){
        tim.stop();
        btn1.setEnabled(true);

        if(arrayRButtons[1].isSelected()
            ||arrayRButtons[5].isSelected()
            ||arrayRButtons[11].isSelected()
            ||arrayRButtons[13].isSelected()
            ||arrayRButtons[16].isSelected()
            ||arrayRButtons[23].isSelected()
            ||arrayRButtons[27].isSelected()
            ||arrayRButtons[29].isSelected()
            ||arrayRButtons[32].isSelected()){
            s+=10;
            JOptionPane.showMessageDialog(null, "Correct");
        } else if(arrayRButtons[36].isSelected()){
            s+=10;
            JOptionPane.showMessageDialog(null, "Correct, you won: "+s+" points");
            btn1.setText("Start again quiz");
        }else if(arrayRButtons[33].isSelected()
                ||arrayRButtons[34].isSelected()
                ||arrayRButtons[35].isSelected()){
            JOptionPane.showMessageDialog(null, "Wrong, you won: "+s+" points");
            btn1.setText("Start again quiz");
        }else{
            JOptionPane.showMessageDialog(null, "Wrong");
        }
        for (int i = 0; i < 10; i++) {
            arrayGroups[i].clearSelection();
        }
        btn2.setEnabled(false);
    }

});

t=10;

//Taimer
lb2=new JLabel("10");
tim=new Timer(1000,new ActionListener(){
    @Override
    public void actionPerformed(ActionEvent e){
        if(t>0){
        t--;
        lb2.setText(String.valueOf(t));
        }else{
            tim.stop();
            JOptionPane.showMessageDialog(null, "Time's up");
            btn2.setEnabled(false); 
            btn1.setEnabled(true);
            }
        }
    });
}

private void startGUI(){
p1.add(lb1);

p3.add(btn1);
p3.add(btn2);
p3.add(lb2);

int q=0;
for(int w=0;w<10;w++){

arrayPanels[w].add(arrayLabels[w]);
arrayPanels[w].add(arrayRButtons[q]);
arrayPanels[w].add(arrayRButtons[q+1]);
arrayPanels[w].add(arrayRButtons[q+2]);
arrayPanels[w].add(arrayRButtons[q+3]);

q+=4;
}

frame.add(p1,BorderLayout.NORTH);
frame.add(p2,BorderLayout.CENTER);
frame.add(p3,BorderLayout.SOUTH);

cl.show(p2, "0");

tim.start();
frame.setVisible(true);

}

public static void main(String[] args) {
Quiz start=new Quiz();
start.startGUI();

}