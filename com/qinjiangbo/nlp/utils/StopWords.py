# coding=utf-8

"""
   Date: 18/11/2016
   Author: qinjiangbo@github.io
   stop words for the documents, which will be removed in the process
"""


class StopWords(object):
    set = set()  # hash set for storing stop words
    INSTANCE = None  # singleton

    @classmethod
    def get_instance(cls):  # class method
        if StopWords.INSTANCE == None:
            StopWords.INSTANCE = StopWords()
        return StopWords.INSTANCE

    def __init__(self):  # instance method
        # Stopwords list from Rainbow
        StopWords.set.add("a")
        StopWords.set.add("able")
        StopWords.set.add("about")
        StopWords.set.add("above")
        StopWords.set.add("according")
        StopWords.set.add("accordingly")
        StopWords.set.add("across")
        StopWords.set.add("actually")
        StopWords.set.add("after")
        StopWords.set.add("afterwards")
        StopWords.set.add("again")
        # StopWords.set.add("against")
        StopWords.set.add("all")
        # StopWords.set.add("allow")
        # StopWords.set.add("allows")
        # StopWords.set.add("almost")
        StopWords.set.add("alone")
        StopWords.set.add("along")
        StopWords.set.add("already")
        StopWords.set.add("also")
        # StopWords.set.add("although")
        StopWords.set.add("always")
        StopWords.set.add("am")
        StopWords.set.add("among")
        StopWords.set.add("amongst")
        StopWords.set.add("an")
        StopWords.set.add("and")
        StopWords.set.add("another")
        StopWords.set.add("any")
        StopWords.set.add("anybody")
        StopWords.set.add("anyhow")
        StopWords.set.add("anyone")
        StopWords.set.add("anything")
        StopWords.set.add("anyway")
        StopWords.set.add("anyways")
        StopWords.set.add("anywhere")
        StopWords.set.add("apart")
        StopWords.set.add("appear")
        # StopWords.set.add("appreciate")
        StopWords.set.add("appropriate")
        StopWords.set.add("are")
        StopWords.set.add("around")
        StopWords.set.add("as")
        StopWords.set.add("aside")
        StopWords.set.add("ask")
        StopWords.set.add("asking")
        StopWords.set.add("associated")
        StopWords.set.add("at")
        StopWords.set.add("available")
        StopWords.set.add("away")
        # StopWords.set.add("awfully")
        StopWords.set.add("b")
        StopWords.set.add("be")
        StopWords.set.add("became")
        StopWords.set.add("because")
        StopWords.set.add("become")
        StopWords.set.add("becomes")
        StopWords.set.add("becoming")
        StopWords.set.add("been")
        StopWords.set.add("before")
        StopWords.set.add("beforehand")
        StopWords.set.add("behind")
        StopWords.set.add("being")
        StopWords.set.add("believe")
        StopWords.set.add("below")
        StopWords.set.add("beside")
        StopWords.set.add("besides")
        # StopWords.set.add("best")
        # StopWords.set.add("better")
        StopWords.set.add("between")
        StopWords.set.add("beyond")
        StopWords.set.add("both")
        StopWords.set.add("but")
        StopWords.set.add("brief")
        StopWords.set.add("by")
        StopWords.set.add("c")
        StopWords.set.add("came")
        StopWords.set.add("can")
        StopWords.set.add("certain")
        StopWords.set.add("certainly")
        StopWords.set.add("clearly")
        StopWords.set.add("co")
        StopWords.set.add("com")
        StopWords.set.add("come")
        StopWords.set.add("comes")
        StopWords.set.add("contain")
        StopWords.set.add("containing")
        StopWords.set.add("contains")
        StopWords.set.add("corresponding")
        StopWords.set.add("could")
        StopWords.set.add("course")
        StopWords.set.add("currently")
        StopWords.set.add("d")
        StopWords.set.add("definitely")
        StopWords.set.add("described")
        StopWords.set.add("despite")
        StopWords.set.add("did")
        StopWords.set.add("different")
        StopWords.set.add("do")
        StopWords.set.add("does")
        StopWords.set.add("doing")
        StopWords.set.add("done")
        StopWords.set.add("down")
        StopWords.set.add("downwards")
        StopWords.set.add("during")
        StopWords.set.add("e")
        StopWords.set.add("each")
        StopWords.set.add("edu")
        StopWords.set.add("eg")
        StopWords.set.add("eight")
        StopWords.set.add("either")
        StopWords.set.add("else")
        StopWords.set.add("elsewhere")
        StopWords.set.add("enough")
        StopWords.set.add("entirely")
        StopWords.set.add("especially")
        StopWords.set.add("et")
        StopWords.set.add("etc")
        StopWords.set.add("even")
        StopWords.set.add("ever")
        StopWords.set.add("every")
        StopWords.set.add("everybody")
        StopWords.set.add("everyone")
        StopWords.set.add("everything")
        StopWords.set.add("everywhere")
        StopWords.set.add("ex")
        StopWords.set.add("exactly")
        StopWords.set.add("example")
        StopWords.set.add("except")
        StopWords.set.add("f")
        StopWords.set.add("far")
        StopWords.set.add("few")
        StopWords.set.add("fifth")
        StopWords.set.add("first")
        StopWords.set.add("five")
        StopWords.set.add("followed")
        StopWords.set.add("following")
        StopWords.set.add("follows")
        StopWords.set.add("for")
        StopWords.set.add("former")
        StopWords.set.add("formerly")
        StopWords.set.add("forth")
        StopWords.set.add("four")
        StopWords.set.add("from")
        StopWords.set.add("further")
        StopWords.set.add("furthermore")
        StopWords.set.add("g")
        StopWords.set.add("get")
        StopWords.set.add("gets")
        StopWords.set.add("getting")
        StopWords.set.add("given")
        StopWords.set.add("gives")
        StopWords.set.add("go")
        StopWords.set.add("goes")
        StopWords.set.add("going")
        StopWords.set.add("gone")
        StopWords.set.add("got")
        StopWords.set.add("gotten")
        # StopWords.set.add("greetings")
        StopWords.set.add("h")
        StopWords.set.add("had")
        StopWords.set.add("happens")
        # StopWords.set.add("hardly")
        StopWords.set.add("has")
        StopWords.set.add("have")
        StopWords.set.add("having")
        StopWords.set.add("he")
        StopWords.set.add("hello")
        StopWords.set.add("help")
        StopWords.set.add("hence")
        StopWords.set.add("her")
        StopWords.set.add("here")
        StopWords.set.add("hereafter")
        StopWords.set.add("hereby")
        StopWords.set.add("herein")
        StopWords.set.add("hereupon")
        StopWords.set.add("hers")
        StopWords.set.add("herself")
        StopWords.set.add("hi")
        StopWords.set.add("him")
        StopWords.set.add("himself")
        StopWords.set.add("his")
        StopWords.set.add("hither")
        # StopWords.set.add("hopefully")
        StopWords.set.add("how")
        StopWords.set.add("howbeit")
        StopWords.set.add("however")
        StopWords.set.add("i")
        StopWords.set.add("ie")
        StopWords.set.add("if")
        # StopWords.set.add("ignored")
        StopWords.set.add("immediate")
        StopWords.set.add("in")
        StopWords.set.add("inasmuch")
        StopWords.set.add("inc")
        StopWords.set.add("indeed")
        StopWords.set.add("indicate")
        StopWords.set.add("indicated")
        StopWords.set.add("indicates")
        StopWords.set.add("inner")
        StopWords.set.add("insofar")
        StopWords.set.add("instead")
        StopWords.set.add("into")
        StopWords.set.add("inward")
        StopWords.set.add("is")
        StopWords.set.add("it")
        StopWords.set.add("its")
        StopWords.set.add("itself")
        StopWords.set.add("j")
        StopWords.set.add("just")
        StopWords.set.add("k")
        StopWords.set.add("keep")
        StopWords.set.add("keeps")
        StopWords.set.add("kept")
        # StopWords.set.add("know")
        # StopWords.set.add("knows")
        # StopWords.set.add("known")
        StopWords.set.add("l")
        StopWords.set.add("last")
        StopWords.set.add("lately")
        StopWords.set.add("later")
        StopWords.set.add("latter")
        StopWords.set.add("latterly")
        StopWords.set.add("least")
        StopWords.set.add("less")
        StopWords.set.add("lest")
        StopWords.set.add("let")
        StopWords.set.add("like")
        StopWords.set.add("liked")
        StopWords.set.add("likely")
        StopWords.set.add("little")
        StopWords.set.add("ll")  # StopWords.set.added to avoid words like you'll,I'll etc.
        StopWords.set.add("look")
        StopWords.set.add("looking")
        StopWords.set.add("looks")
        StopWords.set.add("ltd")
        StopWords.set.add("m")
        StopWords.set.add("mainly")
        StopWords.set.add("many")
        StopWords.set.add("may")
        StopWords.set.add("maybe")
        StopWords.set.add("me")
        # StopWords.set.add("mean")
        StopWords.set.add("meanwhile")
        # StopWords.set.add("merely")
        StopWords.set.add("might")
        StopWords.set.add("more")
        StopWords.set.add("moreover")
        StopWords.set.add("most")
        StopWords.set.add("mostly")
        StopWords.set.add("much")
        StopWords.set.add("must")
        StopWords.set.add("my")
        StopWords.set.add("myself")
        StopWords.set.add("n")
        StopWords.set.add("name")
        StopWords.set.add("namely")
        StopWords.set.add("nd")
        StopWords.set.add("near")
        StopWords.set.add("nearly")
        StopWords.set.add("necessary")
        StopWords.set.add("need")
        StopWords.set.add("needs")
        # StopWords.set.add("neither")
        # StopWords.set.add("never")
        # StopWords.set.add("nevertheless")
        StopWords.set.add("new")
        StopWords.set.add("next")
        StopWords.set.add("nine")
        StopWords.set.add("normally")
        # StopWords.set.add("novel")
        StopWords.set.add("no")
        StopWords.set.add("nobody")
        StopWords.set.add("non")
        StopWords.set.add("none")
        StopWords.set.add("noone")
        StopWords.set.add("nor")
        StopWords.set.add("normally")
        StopWords.set.add("not")
        StopWords.set.add("n't")
        StopWords.set.add("nothing")
        StopWords.set.add("novel")
        StopWords.set.add("now")
        StopWords.set.add("nowhere")
        StopWords.set.add("now")
        StopWords.set.add("nowhere")
        StopWords.set.add("o")
        StopWords.set.add("obviously")
        StopWords.set.add("of")
        StopWords.set.add("off")
        StopWords.set.add("often")
        StopWords.set.add("oh")
        StopWords.set.add("ok")
        StopWords.set.add("okay")
        # StopWords.set.add("old")
        StopWords.set.add("on")
        StopWords.set.add("once")
        StopWords.set.add("one")
        StopWords.set.add("ones")
        StopWords.set.add("only")
        StopWords.set.add("onto")
        StopWords.set.add("or")
        StopWords.set.add("other")
        StopWords.set.add("others")
        StopWords.set.add("otherwise")
        StopWords.set.add("ought")
        StopWords.set.add("our")
        StopWords.set.add("ours")
        StopWords.set.add("ourselves")
        StopWords.set.add("out")
        StopWords.set.add("outside")
        StopWords.set.add("over")
        StopWords.set.add("overall")
        StopWords.set.add("own")
        StopWords.set.add("p")
        StopWords.set.add("particular")
        StopWords.set.add("particularly")
        StopWords.set.add("per")
        StopWords.set.add("perhaps")
        StopWords.set.add("placed")
        StopWords.set.add("please")
        StopWords.set.add("plus")
        StopWords.set.add("possible")
        StopWords.set.add("presumably")
        StopWords.set.add("probably")
        StopWords.set.add("provides")
        StopWords.set.add("q")
        StopWords.set.add("que")
        StopWords.set.add("quite")
        StopWords.set.add("qv")
        StopWords.set.add("r")
        StopWords.set.add("rather")
        StopWords.set.add("rd")
        StopWords.set.add("re")
        StopWords.set.add("really")
        StopWords.set.add("reasonably")
        StopWords.set.add("regarding")
        StopWords.set.add("regardless")
        StopWords.set.add("regards")
        StopWords.set.add("relatively")
        StopWords.set.add("respectively")
        StopWords.set.add("right")
        StopWords.set.add("s")
        StopWords.set.add("said")
        StopWords.set.add("same")
        StopWords.set.add("saw")
        StopWords.set.add("say")
        StopWords.set.add("saying")
        StopWords.set.add("says")
        StopWords.set.add("second")
        StopWords.set.add("secondly")
        StopWords.set.add("see")
        StopWords.set.add("seeing")
        # StopWords.set.add("seem")
        # StopWords.set.add("seemed")
        # StopWords.set.add("seeming")
        # StopWords.set.add("seems")
        StopWords.set.add("seen")
        StopWords.set.add("self")
        StopWords.set.add("selves")
        StopWords.set.add("sensible")
        StopWords.set.add("sent")
        # StopWords.set.add("serious")
        # StopWords.set.add("seriously")
        StopWords.set.add("seven")
        StopWords.set.add("several")
        StopWords.set.add("shall")
        StopWords.set.add("she")
        StopWords.set.add("should")
        StopWords.set.add("since")
        StopWords.set.add("six")
        StopWords.set.add("so")
        StopWords.set.add("some")
        StopWords.set.add("somebody")
        StopWords.set.add("somehow")
        StopWords.set.add("someone")
        StopWords.set.add("something")
        StopWords.set.add("sometime")
        StopWords.set.add("sometimes")
        StopWords.set.add("somewhat")
        StopWords.set.add("somewhere")
        StopWords.set.add("soon")
        StopWords.set.add("sorry")
        StopWords.set.add("specified")
        StopWords.set.add("specify")
        StopWords.set.add("specifying")
        StopWords.set.add("still")
        StopWords.set.add("sub")
        StopWords.set.add("such")
        StopWords.set.add("sup")
        StopWords.set.add("sure")
        StopWords.set.add("t")
        StopWords.set.add("take")
        StopWords.set.add("taken")
        StopWords.set.add("tell")
        StopWords.set.add("tends")
        StopWords.set.add("th")
        StopWords.set.add("than")
        # StopWords.set.add("thank")
        # StopWords.set.add("thanks")
        # StopWords.set.add("thanx")
        StopWords.set.add("that")
        StopWords.set.add("thats")
        StopWords.set.add("the")
        StopWords.set.add("their")
        StopWords.set.add("theirs")
        StopWords.set.add("them")
        StopWords.set.add("themselves")
        StopWords.set.add("then")
        StopWords.set.add("thence")
        StopWords.set.add("there")
        StopWords.set.add("thereafter")
        StopWords.set.add("thereby")
        StopWords.set.add("therefore")
        StopWords.set.add("therein")
        StopWords.set.add("theres")
        StopWords.set.add("thereupon")
        StopWords.set.add("these")
        StopWords.set.add("they")
        StopWords.set.add("think")
        StopWords.set.add("third")
        StopWords.set.add("this")
        StopWords.set.add("thorough")
        StopWords.set.add("thoroughly")
        StopWords.set.add("those")
        StopWords.set.add("though")
        StopWords.set.add("three")
        StopWords.set.add("through")
        StopWords.set.add("throughout")
        StopWords.set.add("thru")
        StopWords.set.add("thus")
        StopWords.set.add("to")
        StopWords.set.add("together")
        StopWords.set.add("too")
        StopWords.set.add("took")
        StopWords.set.add("toward")
        StopWords.set.add("towards")
        StopWords.set.add("tried")
        StopWords.set.add("tries")
        StopWords.set.add("truly")
        StopWords.set.add("try")
        StopWords.set.add("trying")
        StopWords.set.add("twice")
        StopWords.set.add("two")
        StopWords.set.add("u")
        StopWords.set.add("un")
        StopWords.set.add("under")
        # StopWords.set.add("unfortunately")
        # StopWords.set.add("unless")
        # StopWords.set.add("unlikely")
        StopWords.set.add("until")
        StopWords.set.add("unto")
        StopWords.set.add("up")
        StopWords.set.add("upon")
        StopWords.set.add("us")
        StopWords.set.add("use")
        StopWords.set.add("used")
        # StopWords.set.add("useful")
        StopWords.set.add("uses")
        StopWords.set.add("using")
        StopWords.set.add("usually")
        StopWords.set.add("uucp")
        StopWords.set.add("v")
        StopWords.set.add("value")
        StopWords.set.add("various")
        StopWords.set.add("ve")  # StopWords.set.added to avoid words like I've,you've etc.
        StopWords.set.add("very")
        StopWords.set.add("via")
        StopWords.set.add("viz")
        StopWords.set.add("vs")
        StopWords.set.add("w")
        StopWords.set.add("want")
        StopWords.set.add("wants")
        StopWords.set.add("was")
        # StopWords.set.add("way")
        StopWords.set.add("we")
        # StopWords.set.add("welcome")
        # StopWords.set.add("well")
        StopWords.set.add("went")
        StopWords.set.add("were")
        StopWords.set.add("what")
        # StopWords.set.add("whatever")
        StopWords.set.add("when")
        StopWords.set.add("whence")
        StopWords.set.add("whenever")
        StopWords.set.add("where")
        StopWords.set.add("whereafter")
        StopWords.set.add("whereas")
        StopWords.set.add("whereby")
        StopWords.set.add("wherein")
        StopWords.set.add("whereupon")
        StopWords.set.add("wherever")
        StopWords.set.add("whether")
        StopWords.set.add("which")
        StopWords.set.add("while")
        StopWords.set.add("whither")
        StopWords.set.add("who")
        StopWords.set.add("whoever")
        StopWords.set.add("whole")
        StopWords.set.add("whom")
        StopWords.set.add("whose")
        StopWords.set.add("why")
        StopWords.set.add("will")
        StopWords.set.add("willing")
        StopWords.set.add("wish")
        StopWords.set.add("with")
        StopWords.set.add("within")
        StopWords.set.add("without")
        StopWords.set.add("wonder")
        StopWords.set.add("would")
        StopWords.set.add("would")
        StopWords.set.add("x")
        StopWords.set.add("y")
        # StopWords.set.add("yes")
        StopWords.set.add("yet")
        StopWords.set.add("you")
        StopWords.set.add("your")
        StopWords.set.add("yours")
        StopWords.set.add("yourself")
        StopWords.set.add("yourselves")
        StopWords.set.add("z")
        StopWords.set.add("zero")
        StopWords.set.add("i'm")
        StopWords.set.add("he's")
        StopWords.set.add("she's")
        StopWords.set.add("you're")
        StopWords.set.add("i'll")
        StopWords.set.add("you'll")
        StopWords.set.add("she'll")
        StopWords.set.add("he'll")
        StopWords.set.add("it's")
        StopWords.set.add("don't")
        StopWords.set.add("can't")
        StopWords.set.add("didn't")
        StopWords.set.add("i've")
        StopWords.set.add("that's")
        StopWords.set.add("there's")
        StopWords.set.add("isn't")
        StopWords.set.add("what's")
        StopWords.set.add("rt")
        StopWords.set.add("doesn't")
        StopWords.set.add("w/")
        StopWords.set.add("w/o")

    # remove all stopwords
    def clear(self):
        StopWords.set.clear()

    # add the word to set
    # @param word
    def add(self, word):
        if len(word.strip()) > 0:  # trim blanks in both sides
            StopWords.set.add(word.lower())

    # remove the word from set
    # @param word
    def remove(self, word):
        StopWords.set.remove(word)
        return word