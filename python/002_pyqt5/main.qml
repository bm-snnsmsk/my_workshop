import QtQuick.Window 2.2
import QtQuick 2.3

Window{
    visible:true
    width:600
    height:400
    color:"green"
    titile:"PyQt5 QML"

Row{ // Column   // satır sutun
    Rectangle{
    color:red
    width:360/3
    height:360/1.2
}
Rectangle{
    color:blue
    width:360/3
    height:360/1.2
}
Rectangle{
    color:yellow
    width:360/3
    height:360/1.2
}
}

Text{
    id:mytext
    text="hello QML"
    font.pixelSize:30
    font.bold:true
    color:"white"
    anchors.centerIn:parent
}

Image{
    id:image
    source:"qml.png"
    sourceSize.width:parent.width/2
    sourceSize.height:parent.height/2
}

TextInput{
   id:te 
   text:"hello"
   color:"red"
   //scale:6
   font.pixelSize:16; font.bold:true
   x:200
   y:100
   focus:true
   maximumLength:16
   font.capitalization:Font.AllUppercase
}
}