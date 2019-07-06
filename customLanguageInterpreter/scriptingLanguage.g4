/*
 * Name of the Grammar (must be the same as the file name)
 */
grammar scriptingLanguage;

/*
 * Parser Rules
 */

// Test suite declaration
suite       :   WHEN apptype APP COL testlist;
apptype     :   APPCAT1 | APPCAT2 | APPCAT3 | APPCAT4 | APPCAT5 | APPCAT6 | APPCAT7 | APPCAT8 | APPCAT9 | APPCAT10;

// Specific test declaration
testlist    :   (testtype1 | testtype2 | testtype3 | testtype4 | testtype5 | testtype6 | testtype7 | testtype8)+;
testtype1   :   (testsame1 | testdiff1);
testtype2   :   (testsame2 | testdiff2);
testtype3   :   (testsame3 | testdiff3);
testtype4   :   (testsame4 | testdiff4);
testtype5   :   (testsame5 | testdiff5);
testtype6   :   (testsame6 | testdiff6);
testtype7   :   (testsame7 | testdiff7);
testtype8   :   (testsame8 | testdiff8);

// (ALL THOSE DECLARATIONS ARE NEEDED SO THAT WE CAN CHECK IF A COMMAND IS VALID FOR A SPECIFIC ACTIVITY TYPE AT PARSER LEVEL)
testsame1   :   IN ACTTYPE1 CHECK FOR SAME STATE COL commandlist1;
testdiff1   :   IN ACTTYPE1 CHECK FOR DIFFERENT STATE activitytype COL commandlist1;
testsame2   :   IN ACTTYPE2 CHECK FOR SAME STATE COL commandlist2;
testdiff2   :   IN ACTTYPE2 CHECK FOR DIFFERENT STATE activitytype COL commandlist2;
testsame3   :   IN ACTTYPE3 CHECK FOR SAME STATE COL commandlist3;
testdiff3   :   IN ACTTYPE3 CHECK FOR DIFFERENT STATE activitytype COL commandlist3;
testsame4   :   IN ACTTYPE4 CHECK FOR SAME STATE COL commandlist4;
testdiff4   :   IN ACTTYPE4 CHECK FOR DIFFERENT STATE activitytype COL commandlist4;
testsame5   :   IN ACTTYPE5 CHECK FOR SAME STATE COL commandlist5;
testdiff5   :   IN ACTTYPE5 CHECK FOR DIFFERENT STATE activitytype COL commandlist5;
testsame6   :   IN ACTTYPE6 CHECK FOR SAME STATE COL commandlist6;
testdiff6   :   IN ACTTYPE6 CHECK FOR DIFFERENT STATE activitytype COL commandlist6;
testsame7   :   IN ACTTYPE7 CHECK FOR SAME STATE COL commandlist7;
testdiff7   :   IN ACTTYPE7 CHECK FOR DIFFERENT STATE activitytype COL commandlist7;
testsame8   :   IN ACTTYPE8 CHECK FOR SAME STATE COL commandlist8;
testdiff8   :   IN ACTTYPE8 CHECK FOR DIFFERENT STATE activitytype COL commandlist8;

activitytype    :   ACTTYPE1 | ACTTYPE2 | ACTTYPE3 | ACTTYPE4 | ACTTYPE5 | ACTTYPE6 | ACTTYPE7 | ACTTYPE8;

// Definition of commands for tests related to a specific Activity type
// To-do screen
commandlist1    :   ( (command1ver1|command1ver2|command1ver3|command1ver4|command1ver5|command1ver6|command1ver7|commandCustomClick|commandCustomLongClick|commandCustomDrag|commandCustomType|commandCustomBack|testCustom) SEMICOL)+;
command1ver1    :   ADD TASK QUOTEDSTRING;
command1ver2    :   TICK LINE NUMBER;
command1ver3    :   TICK ALL;
command1ver4    :   CLICK LINE NUMBER;
command1ver5    :   PRESS BACK;
command1ver6    :   SWIPE UP;
command1ver7    :   SWIPE DOWN;
// Ads screen
commandlist2    :   ( (command2ver1|command2ver2|command2ver3|commandCustomClick|commandCustomLongClick|commandCustomDrag|commandCustomType|commandCustomBack|testCustom) SEMICOL)+;
command2ver1    :   CLICK CLOSE;
command2ver2    :   CLICK ACTTYPE2;
command2ver3    :   PRESS BACK;
// Login screen
commandlist3    :   ( (command3ver1|command3ver2|command3ver3|commandCustomClick|commandCustomLongClick|commandCustomDrag|commandCustomType|commandCustomBack|testCustom) SEMICOL)+;
command3ver1    :   INPUT NAME QUOTEDSTRING;
command3ver2    :   INPUT PASSWORD QUOTEDSTRING;
command3ver3    :   CLICK NEXT;
// List screen
commandlist4    :   ( (command4ver1|command4ver2|command4ver3|command4ver4|command4ver5|command4ver6|command4ver7|commandCustomClick|commandCustomLongClick|commandCustomDrag|commandCustomType|commandCustomBack|testCustom) SEMICOL)+;
command4ver1    :   CLICK LINE NUMBER;
command4ver2    :   TOGGLE LINE NUMBER;
command4ver3    :   LONG CLICK LINE NUMBER;
command4ver4    :   LONG CLICK ALL;
command4ver5    :   PRESS BACK;
command4ver6    :   SWIPE UP;
command4ver7    :   SWIPE DOWN;
// Portal screen
commandlist5    :   ( (command5ver1|command5ver2|command5ver3|command5ver4|commandCustomClick|commandCustomLongClick|commandCustomDrag|commandCustomType|commandCustomBack|testCustom) SEMICOL)+;
command5ver1    :   SWIPE UP;
command5ver2    :   SWIPE DOWN;
command5ver3    :   SWIPE LEFT;
command5ver4    :   SWIPE RIGHT;
// Browser screen
commandlist6    :   ( (command6ver1|command6ver2|command6ver3|commandCustomClick|commandCustomLongClick|commandCustomDrag|commandCustomType|commandCustomBack|testCustom) SEMICOL)+;
command6ver1    :   INPUT URL QUOTEDSTRING;
command6ver2    :   PRESS ENTER;
command6ver3    :   PRESS BACK;
// Map screen
commandlist7    :   ( (command7ver1|command7ver2|command7ver3|command7ver4|command7ver5|command7ver6|command7ver7|commandCustomClick|commandCustomLongClick|commandCustomDrag|commandCustomType|commandCustomBack|testCustom) SEMICOL)+;
command7ver1    :   INPUT SEARCH QUOTEDSTRING;
command7ver2    :   SWIPE UP;
command7ver3    :   SWIPE DOWN;
command7ver4    :   SWIPE LEFT;
command7ver5    :   SWIPE RIGHT;
command7ver6    :   CLICK CENTER;
command7ver7    :   LONG CLICK CENTER;
// Messages screen
commandlist8    :   ( (command8ver1|command8ver2|command8ver3|command8ver4|command8ver5|commandCustomClick|commandCustomLongClick|commandCustomDrag|commandCustomType|commandCustomBack|testCustom) SEMICOL)+;
command8ver1    :   INPUT MESSAGE QUOTEDSTRING;
command8ver2    :   PRESS ENTER;
command8ver3    :   PRESS BACK;
command8ver4    :   SWIPE UP;
command8ver5    :   SWIPE DOWN;


// Custom commands that can be used anywhere
commandCustomClick  :   CUSTOM CLICK XPOINT YPOINT;
commandCustomLongClick  :   CUSTOM LONG CLICK XPOINT YPOINT;
commandCustomDrag   :   CUSTOM DRAG FROM XPOINT YPOINT TO XPOINT YPOINT DURATION NUMBER;
commandCustomType   :   CUSTOM TYPE QUOTEDSTRING;
commandCustomBack   :   CUSTOM PRESS DEVICE BACK;

// Command to execute pre-made tests
testCustom  :   EXECUTE (testSlot1|testSlot2|testSlot3);
testSlot1   :   TESTSLOT1;
testSlot2   :   TESTSLOT2;
testSlot3   :   TESTSLOT3;


/*
 * Lexer Rules
 */

// Fragments are used for case-insensitivity
fragment A : [aA];
fragment B : [bB];
fragment C : [cC];
fragment D : [dD];
fragment E : [eE];
fragment F : [fF];
fragment G : [gG];
fragment H : [hH];
fragment I : [iI];
fragment J : [jJ];
fragment K : [kK];
fragment L : [lL];
fragment M : [mM];
fragment N : [nN];
fragment O : [oO];
fragment P : [pP];
fragment Q : [qQ];
fragment R : [rR];
fragment S : [sS];
fragment T : [tT];
fragment U : [uU];
fragment V : [vV];
fragment W : [wW];
fragment X : [xX];
fragment Y : [yY];
fragment Z : [zZ];

// Declaration of words with fragments
WHEN        :   W H E N;
APP         :   A P P;
COL         :   ':';
SEMICOL     :   ';';
IN          :   I N;
CHECK       :   C H E C K;
FOR         :   F O R;
SAME        :   S A M E;
DIFFERENT   :   D I F F E R E N T;
STATE       :   S T A T E;
INPUT       :   I N P U T;
NAME        :   N A M E;
PASSWORD    :   P A S S W O R D;
CLICK       :   C L I C K;
NEXT        :   N E X T;
CLOSE       :   C L O S E;
PRESS       :   P R E S S;
BACK        :   B A C K;
LINE        :   L I N E;
LONG        :   L O N G;
ALL         :   A L L;
URL         :   U R L;
ENTER       :   E N T E R;
MESSAGE     :   M E S S A G E;
TOGGLE      :   T O G G L E;
SWIPE       :   S W I P E;
UP          :   U P;
DOWN        :   D O W N;
LEFT        :   L E F T;
RIGHT       :   R I G H T;
SEARCH      :   S E A R C H;
CENTER      :   C E N T E R;
TICK        :   T I C K;
ADD         :   A D D;
TASK        :   T A S K;
CUSTOM      :   C U S T O M;
DRAG        :   D R A G;
XPOINT      :   NUMBER;
YPOINT      :   NUMBER;
FROM        :   F R O M;
TO          :   T O;
DURATION    :   D U R A T I O N;
TYPE        :   T Y P E;
DEVICE      :   D E V I C E;
EXECUTE     :   E X E C U T E;
TESTSLOT1   :   T E S T S L O T [1];
TESTSLOT2   :   T E S T S L O T [2];
TESTSLOT3   :   T E S T S L O T [3];

// Application APK categories
APPCAT1     :   N E W S;
APPCAT2     :   S H O P P I N G;
APPCAT3     :   S O C I A L;
APPCAT4     :   V I D E O;
APPCAT5     :   W E A T H E R;
APPCAT6     :   C O M M U N I C A T I O N;
APPCAT7     :   E D U C A T I O N;
APPCAT8     :   F O O D;
APPCAT9     :   M E D I C A L;
APPCAT10    :   A U D I O;

// Activity type categories
ACTTYPE1    :   T O D O;
ACTTYPE2    :   A D;
ACTTYPE3    :   L O G I N;
ACTTYPE4    :   L I S T;
ACTTYPE5    :   P O R T A L;
ACTTYPE6    :   B R O W S E R;
ACTTYPE7    :   M A P;
ACTTYPE8    :   M E S S A G E S;



QUOTEDSTRING        : '"'[-a-zA-Z0-9!@#$&()`.+,]*'"';
WHITESPACE          : (' ' | '\t')+ -> skip;
NEWLINE             : ('\r'? '\n' | '\r')+ -> skip;
NUMBER              : [0-9]+[.]?[0-9]*;



