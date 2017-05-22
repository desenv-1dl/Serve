# -*- coding: utf-8 -*-

'''################### estilos para todo os objetos do plugin ###################'''

buttonRoutineStyle = '''QPushButton{
                        height: 70;
                        font: 75 bold 10pt \"Cantarell\";
                        text-align:center;
                        border-top: 4px solid;
                        border-bottom: 4px solid;
                        border-left: 4px solid;
                        border-right: 4px solid;
                        image: url(:/plugins/FmeServer/routine1.png);
                        image-position: left;
                        background:  #285663;
                        color: rgb(255, 255, 255);
                        }
                   
                        QPushButton:checked{
                        image: url(:/plugins/FmeServer/routine2.png);
                        image-position: left;
                        }'''

routineAreaStyle = '''QWidget {
                      background:  #285663;
                      border: 1px solid  #100c08;
                      }'''
                        
labelDescriptionStyle = '''QLabel {
                           font: 9pt \"Droid Sans Fallback\";
                           qproperty-wordWrap: true;
                           qproperty-alignment: AlignCenter;
                           border-top: 0px solid;
                           border-bottom: 2px solid;
                           border-left: 0px solid;
                           border-right: 0px solid;
                           color: white;
                           }'''
                            
labelFieldStyle = '''font: 10pt \"Droid Sans Fallback\";
                     qproperty-wordWrap: true;
                     qproperty-alignment: AlignCenter;
                     border: 0px;
                     color: white;'''
                     
labelVersionStyle = '''QLabel {
                           font: 11pt \"Droid Sans Fallback\";
                           qproperty-wordWrap: true;
                           qproperty-alignment: AlignCenter;
                           border-top: 0px solid;
                           border-bottom: 2px solid;
                           border-left: 0px solid;
                           border-right: 0px solid;
                           color: white;
                           }'''
                     
comboFieldStyle = '''QComboBox { 
                     border-radius: 8px;
                     border: 4px solid  #100c08;
                     color:rgb(0, 0, 0); 
                     background-color: rgb(255, 255, 255);
                     font: 8pt \"Monospace\";
                     }
                     
                     QComboBox:focus {
                     border:4px outset; 
                     border-radius: 8px; 
                     border-color: #0892d0;
                     color:rgb(0, 0, 0);
                     }'''
                     
lineEditFieldStyle = '''QLineEdit { 
                        border-radius: 8px;
                        border: 4px solid  #100c08;
                        color:rgb(0, 0, 0); 
                        background-color: rgb(255, 255, 255);
                        font: 8pt \"Monospace\";
                        }
                        QLineEdit:focus {
                        border:4px outset; \n"
                        border-radius: 8px; \n"
                        border-color: #0892d0; \n"
                        color:rgb(0, 0, 0); \n"
                        }'''
                            
buttonFormStyle = '''QPushButton{
                     font: bold 14pt \"Droid Sans Fallback\";
                     background: #00ff40;
                     height: 50px;
                     border-radius: 10px;
                     }'''
                     
progressBarStyle = '''QProgressBar {
                      border: 4px solid  #100c08;
                      }
                      QProgressBar::chunk {
                      background-color: #98fb98;
                      width: 10px;
                      margin: 0.5px;
                      border: 0.6px solid #100c08;
                      }''' 
                            


                  
                            
                            