# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#define narrator = nvl_narrator
define n = Character("", colour="#00000000", kind=nvl_narrator)
define a = Character("Alisia", color="#fffd7b")
define la = Character("Mała Alisia", color="#fffd7b")
define c = Character("Cotard", color="#9c1908")
define lc = Character("Mały Cotard", color="#9c1908")
define bee = Character("Przczułka", color = "#ffa600")
define unon = Character("???", color = "#ffffff")
define u = Character("Uczniowie", color = "#a1fd28")
define f = Character("Ojciec", color="#0077ff")
define m = Character("Matka", color="#00ffd5")
define m1 = Character("Mężczyzna 1", color="#ff5050")
define m2 = Character("Mężczyzna 2", color="#ffae00")
define om = Character("Stary Mężczyzna", color="#474747")
define k1 = Character("Kobieta 1", color="#b9009a")
define k2 = Character("Kobieta 2", color="#7700ff")



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg mountain.png" or "bg mountain.jpg") to the
    # images directory to show it.

    scene bg mountain

    # These display lines of dialogue.
    n "Jestem osobą, która pyta.{w=1}\ Nie potrafię inaczej, nigdy nie potrafiłam."
    n "Pytam o wszystko, jakby ktoś zapisał we mnie wewnętrzny przymus aby zrozumieć niezrozumiałe."
    n "Pociąga mnie to co jeszcze nienazwane, niewypowiedziane, o których inni boją się nawet pomyśleć."

    n "Dratoc pojawił się w naszym życiu niespodziewanie."
    n "Pewnego dnia rodzice po prostu przyszli z nim do domu, i tak już zostało."
    n "Znaleźli go na wybrzeżu, gdzie spacerowali."
    n "Nigdy nie dowiedziałam się kto go tam porzucił i dlaczego."
    n "Ale to nieważne."
    n "Liczyło się dla mnie tylko to, że został."
    n "Dołączył do naszej rodziny jako jej pełnoprawna część."

    n "Nie rozumiem tego, co wydarzyło się później.{w=1}\ Przecież było idealnie."
    n "Ale wtedy rodzice postanowili wyruszyć w Nicość."
    n "Bez wyjaśnień i bez pożegnań.{w=1}\ Poszli tam, gdzie nikt się nie zapuszcza."
    n "Po co?"
    n "W końcu jeszcze nikt stamtąd nie wrócił."

    n "To wydarzenie strzaskało moją potrzebę rozumienia wszystkiego."
    n "Oto bowiem stało się coś, czego zrozumieć nie mogłam i nadal nie mogę."

    n "Może to okrutne, ale uważam, że moi rodzice nigdy nie myśleli trzeźwo."
    n "Choć jestem im za to wdzięczna, zabrali do domu obce dziecko i potraktowali jak własne."
    n "Kto normalny tak robi?!"

    n "Zawsze wszystko robili po swojemu."
    n "Nasze wychowanie nie odbiegało od dziwnego schematu, w którym postanowili uczyć nas samodzielnie w domu zamiast posłać do szkoły."
    n "Gdy skończyłam cztery wiosny uczyli nas zielarstwa i podstawowej pierwszej pomocy."
    n "Gdy skończyłam szóstą wiosnę umiałam już polować i przyrządzać zwierzęta."

    n "Na Górze nie miałam nikogo, rodzice przypłynęli tu z kontynentu."
    n "Zostaliśmy więc zupełnie sami."
    n "Wylądowaliśmy w sierocińcu."
    n "Było to dobre i bezpieczne miejsce, a nasi opiekunowie pełni pasji i miłości do dzieci."
    n "Ale nie byli NIMI."
    n "Samotność i poczucie opuszczenia pożerały nas od środka."
    n "Dobrze, że mieliśmy choć siebie."

    n "Już dosyć wcześnie interesowałam się pracą społeczną i pomaganiem innym."
    n "Zaczęłam się przyglądać, a potem uczestniczyć w opiece nad innymi dziećmi."
    n "Stopniowo dochodziłam do siebie."
    n "Dorastając znów czułam pociąg do zdobywania wiedzy, by potem dzielić się nią z innymi."
    n "Było więc oczywiste, że zostanę nauczycielką."

    n "Wiedza jest bezcenna - bo pozwala oswoić strach."

    n "Zaś co do Dratoca…"
    n "Zniknięcie rodziców zmieniło go."
    n "Nie zauważyłam tego od razu."
    n "Coś w nim pękło."
    n "Z czasem ta szczelina rosła i rosła, aż pochłonęła go w całości."
    n "Zamykał się w sobie, odcinał."
    n "Przeraziło mnie, gdy pewnego dnia stwierdził, że nie ma go już."
    n "Że nie istnieje."

    n "Oświadczył też, że przestał być Dratocem, a zaczął…"
    n "Cotardem."
    n "Reagował wyłącznie na swoje nowe imię."
    n "Próbowałam walczyć, ale co mogłam zrobić?"
    n "Mogłam się z nim porozumieć tylko wtedy, gdy ulegałam i zwracałam się do niego tak, jak chciał."
    n "Inni o dziwo nie zwracali uwagi."
    n "Nie obchodziło to ich tak, jak mnie."

    n "Stał się chłodny. Cichy."
    n "Nie był już dzieckiem, które poznałam i uznałam za swojego małego braciszka."
    n "Dawniej potrafił gadać bez końca, topił mnie w potoku słów."
    n "Ale już nie."
    n "Odzywa się tylko wtedy, gdy uzna to za konieczne."
    n "Czyli prawie nigdy."

    n "Ale wciąż uważam go za mojego brata."
    n "Zawsze będę. Kocham go całym sercem."

    n "To postępuje."
    n "Zmuszam go do posiłków, sam najchętniej nic by nie jadł."
    n "Twierdzi, że nie potrzebuje jedzenia."
    n "Tylko moje łzy i błagania skutkują."
    n "Choć do straszne, znajduję w tym pocieszenie - oznacza bowiem, że mój brat nadal czuje emocje. Nadal mu zależy."
    n "To dla mnie znaczy wszystko."

    n "Ubrania zużywają się na nim jak drewno w ognisku."
    n "Wrzucam je potajemnie, żeby nie zobaczył zaschniętych śladów krwi i oderwanych kawałków skóry."
    n "Przeraża mnie to."
    n "Cotard ropieje, jego skóra pęka, pokrywa się pęcherzami i liszajem."
    n "Nie mówi mi skąd się to bierze."
    n "Ale ja wiem."

    n "Kiedy próbuje zdecynferkować jego rany, on spokojnie odmawia."
    n "Mówi, że tego nie potrzebuje."
    n "Tutaj mój płacz nie pomaga."
    n "NIC nie pomaga."
    n "NIC."

    n "Nigdy nie chodzi z nami do gorących źródeł."
    n "Pytałam, czy chodzi o rany, ale stwierdził, że nie."
    n "Po prostu nie chce."
    n "Myśli, że nie widzę jego reakcji na wodę."
    n "Unika jej jak trucizny. "
    n "Nie myje się."
    n "Cichnie chorobą, ale o dziwo nie jest chory."
    n "O co w tym chodzi…"

    n "Pije tylko grzybowy napar. Dobrze, że chociaż tyle."

    n "Wiem już na pewno, ale nikomu nie powiem."
    n "On chodzi do Nicości."
    n "Jest jedynym, który w Niej był i wrócił."
    n "Próbowałam go o to pytać, ale udaje, że nie słyszy."
    n "Zamyka się zupełnie i mnie odcina,"
    n "Nie zaprzecza."
    n "Po prostu stawia przede mną mur."

    n "Praca w prosektorium mu pomaga."
    n "Mało kto go tam ogląda, a sam Cotard dobrze się czuje wśród zmarłych."
    n "Zupełnie, jakby był jednym z nich."

    n "Dopiero po czasie zrozumiałam, że Cotard nie ma węchu."
    n "Do domu wraca uśmiechnięty, zadowolony."
    n "Zamyka się w szopie i siedzi w niej do następnego dnia."
    n "Rano idzie do pracy. I tak dzień w dzień."

    n "Nieraz próbowałam się włamać do jego kryjówki, ale nic z tego."
    n "Kłódka jest mocna, a łańcuchy dobrej jakości. Drzwi mocne."
    n "Z wnętrza dobiega dziwny jęk."
    n "Boję się."

    n "Ludzie dziwnie na nas patrzą."
    n "Gdyby tylko umieli w nim dostrzec, co ja…"

    n "Wczoraj spytałam go co robi w tej swojej szopie"
    n "Powiedziałam, że chcę wiedzieć BO MAM PRAWO."
    n "Uśmiechnął się tylko i odparł, że to niespodzianka."
    n "NIESPODZIANKA?"
    n "Ile lat to już trwa"
    n "PO CO?"
    n "DLA KOGO?"
    n "Pogłaskał mnie po głowie mówiąc: “Już niedługo siostrzyczko. Zobaczysz. Już niedługo”"
    n "Zaczęłam płakać."
    nvl clear

label Chapter_1:

    scene bg void entrance

    n "{size=+20}Dziennik Alysii Wpis 001{/size}"

    n "Dla moich uczniów"

    n "Jeśli czytacie te słowa, to wiecie już, że jestem w miejscu, do którego nikt nie powinien wchodzić."
    n "On… mówił mi, żebym tego nie robiła."
    n "Że nie wszystko jest do odkrycia."
    n "Że niektóre tajemnice istnieją tylko po to, by pozostać tajemnicami."

    n "Ale jeśli świat ma sens, to musi istnieć jego źródło."

    n "A jeśli go nie ma…"
    n "…to chcę wiedzieć dlaczego."

    n "Nie idę tam jako bohaterka."
    n "Idę jako nauczycielka, która nie potrafi znieść niewiedzy."

    n "Chcę wiedzieć, co się stało z moimi rodzicami."

    n "I nie jestem sama."
    n "Nie martwcie się."
    n "{b}On się mną zaopiekuje.{/b}"
    nvl clear
    n "{b}{size=+60}Rozdział Pierwszy{/size}{/b}"
    n "Wiatr… jest dziwnie cichy"
    n "Nie zimny. Nie ciepły."
    n "Po prostu… czuć, że pochodzi z Nicości."
    
    n "Ogromny krater ciągnie się w dół, jakby świat został wyrwany z własnego ciała."
    
    n "Alysia staje na krawędzi."
    n "A obok niej "
    n "Cotard."
    nvl clear

    a "…to tutaj."
    c "Nie."
    c "…"
    c "Tu nic nie ma."

    "Alysia wybucha lekkim śmiechem"

    a "Właśnie dlatego tu jesteśmy."

    "Cotard patrzy w dół."
    "Długo."
    "Zbyt długo."

    c "Nie czuję strachu."
    c "…"
    c "To nie jest odwaga."

    menu:
        "Wiem, to głupota.":
            jump choice1chapter1_1
        "Dlaczego tak mówisz?":
            jump choice1chapter1_2

    label choice1chapter1_1:
    c "To dobrze."
    c "Przynajmniej to się nie zmieniło"
    jump choice1chapter1_done

    label choice1chapter1_2:
    c "Bo ja i tak nie istnieję."
    c "A jednak nadal potrafię popełniać błędy."
    jump choice1chapter1_done

    label choice1chapter1_done:
    "Pierwszy krok."
    "Ziemia nie wydaje dźwięku."

    a "Słyszysz to?"

    c "Nie"
    c "…i właśnie to powinno cię martwić."

    a "Jesteś jedyną osobą, która może tam wejść i wrócić."

    "Cotard przekrzywia głowę jakby analizował coś czego nie da się zrozumieć"

    c "Boje się, jak na Ciebie zadziała to otoczenie."

    menu:
        "Też się martwię":
            jump choice2chapter1_1
        "Przekonamy się.":
            jump choice2chapter1_2
    label choice2chapter1_1:
    a "Też się martwię."
    a "Boję się, że nagle coś się zmieni i Nicość zacznie działać również na ciebie."
    a "Że odbierze mi nawet tę pewność, którą teraz mam."
    a "Ale… przekonamy się, gdy dojdziemy do Kwiecistej Nicości."

    "Cotard patrzy na nią długo."
    "Jego twarz pozostaje niemal nieruchoma, ale głos staje się cichszy."


    c "…"
    c "Nie martw się o mnie."
    c "Na mnie już Nicość wypróbowała wszystko, co mogła."
    c "…"

    a "Nieprawda."
    a "Gdyby zrobiła wszystko, nie szedłbyś teraz obok mnie."

    "Cotard milknie."
    "Jakby nie potrafił znaleźć odpowiedzi."
    "Po chwili rusza dalej."

    c "…to nie jest argument."

    "Alysia lekko się uśmiecha."
    a "Jest."
    jump choice2chapter1_done

    label choice2chapter1_2:
    a "Przekonamy się z czasem."
    a "Mam nadzieję, że po prostu nic nam się nie stanie"
    a "Może to miejsce tylko tylko próbuje nas przestraszyć."

    "Spogląda w nicość"

    c "Dziwne."
    c "Ludzie zawsze próbują nadać sens temu, czego się boją."
    c "Jakby nazwanie lęku czyniło go mniejszym."

    a "A ty?"
    a "Na czym budujesz strój spokój"

    c "Na pustce."
    c "Nie oczekuję już niczego dobrego."

    a "A ja właśnie odwrotnie."
    a "Oczekuje, że damy sobie radę."
    a "Dlatego dobrze, że idziemy razem."
    jump choice2chapter1_done

    label choice2chapter1_done:
    c "Nie odwracaj się."
    c "Już tego nie ma."

    a "Czego?"

    c "Góry."
    c "Zapomniałem jak wyglądała."

    menu:
        "Co?! To się dzieje za szybko…":
            jump choice3chapter1_1
        "Zauważyłam już… i to mnie przeraża.":
            jump choice3chapter1_2

    label choice3chapter1_1:
    c "Nie przesadzaj"
    c "To normalne."
    jump choice3chapter1_done

    label choice3chapter1_2:
    c "To normalne."
    c "Przyzwyczaisz się."
    jump choice3chapter1_done

    label choice3chapter1_done:
    "Po tych słowach Cotard rusza dalej."
    "Jego kroki są ciche."
    "Nie dlatego, że stawia je lekko,"
    "Po prostu Nicość nie oddaje dźwięku"
    "Alysia idzie tuż za nim"
    "Im niżej schodzą, tym bardziej powietrze staje się…"
    "inne"
    "Nie cięższe."
    "Nie rzadsze."
    "Po prostu obce."
    "Jakby nie należało do świata."

    a "Cotard…"
    a "Czy to tylko mi sie wydaje, czy powietrze tutaj pachnie inaczej?"

    "Cotard zatrzymuje się na moment" 
    "Unosi głowę."


    c "Tak."
    c "Wszystko zaczyna się tutaj."

    a "Co takiego?"

    c "Pierwszy poziom."
    c "Kwiecista Nicość."

    n "Powietrze robi się słodkie."
    n "Zbyt słodkie."
    n "Duszące."
    n "W oddali zaczynają się wyłaniać pierwsze kwiaty."
    n "Delikatne."
    n "Białe."
    n "Ich płatki poruszają się mimo, że nie ma wiatru"
    nvl clear

    scene bg flower plain
    "Z zachwytem"
    a "Och…"
    a "Cotard!"
    a "spójrz tylko"
    a "Jak tu pięknie!"

    "Na jej twarzy pojawia się prawdziwy, ciepły uśmiech."
    "Pierwszy od wejścia."

    c "{size=+20}Nie podchodź!{/size}"

    menu:
        "Dlaczego? Są niebezpieczne?":
            jump choice4chapter1_1
        "Chcesz powiedzieć, że to…?":
            jump choice4chapter1_2

    label choice4chapter1_1:
    "Cotard patrzy na kwiaty."

    "Jeden z płatków drży"
    "Potem cofa się."
    "Jakby czas na moment się załamał."

    c "Nie."
    c "Gorzej."
    c "Chcą, abyś została."

    a "Kwiaty?"

    c "Nie."
    c "Całe to miejsce."
    jump choice4chapter1_done

    label choice4chapter1_2:
    "Dotyka jednego z kwiatów."

    "Jeden z płatków drży"
    "Potem cofa się."
    "Jakby czas na moment się załamał."
    
    c "Tak samo jak ja." 
    c "Też powoli znikam."

    a "Nie mów tak."

    c "Dlaczego?"
    c "Ty jedyna nie próbujesz mi wmówić, że żyję."
    jump choice4chapter1_done

    label choice4chapter1_done:

    n "{size=+20}Dziennik Alysii Wpis 002{/size}"

    n "Kwiaty."
    n "Nie potrafię opisać ich piękna."
    n "Są zbyt doskonałe."
    n "A przez to nienaturalne."

    n "Cotard twierdzi, że nie są prawdziwe."
    n "I co najgorsze…"

    n "wierzę mu."

    n "Mam jednak dziwne wrażenie, że to miejsce reaguje na emocje."
    n "Na zachwyt."
    n "Na lęk."
    n "Na wspomnienia."

    n "Im bardziej chcę coś zrozumieć, tym bardziej rzeczywistość wydaje się miękka."
    n "Jakby można ją było rozerwać palcami."

    nvl clear

    n "Kwiaty drżą."
    n "Pył unosi się w powietrzu jak złoty dym."
    n "Z głębi łąki dobiega dźwięk."
    n "Coś bardziej pomiędzy śmiechem a buczeniem"
    nvl clear
    unon "PRRRRRRRRRRR."

    "Coś małego przelatuje tuż przed twarzą Alysii."
    "Odruchowo cofa się o krok."
    "Przed nimi zawisa drobna istota."

    bee "Prrr–prrrr!"
    bee "OoooOOOO, goście!"
    bee "Żywi goście!"

    "Przekrzywia głowę."
    "Patrzy na Cotarda."

    c "…"

    bee "Hhahahahahahahahha"
    bee "A nie."
    bee "nie wszyscy"
    bee "PRRRR."

    "Zaczyna latać wokół niego."

    bee "Ty śmierdzisz!"
    bee "Fuj FUJ FUUUJJJ"
    bee "Jak stare liście."
    bee "Jak mokry grób."
    bee "Jak coś, co już dawno powinno zostać na dole."
    bee "Prawda Cotard?"

    "Cotard patrzy na nią pustym wzrokiem."

    c "Odejdź."

    bee "Oooodejdź."
    bee "Ooooo odeeejdźź"
    bee "Prrrrrrr."

    "Alysia mimowolnie się uśmiecha."
    "Trochę nerwowo"
    "Trochę rozbawiona"

    a "Jesteś… mieszkanką tego miejsca?"

    bee "A ty jesteś śmieszna."
    bee "Prrr."
    bee "Pytasz tak, jakby to miejsce miało mieszkańców."
    bee "To miejsce ma tylko to, co zostało"
    bee "I to jest SUUUUUUUUUUUUPER"

    a "A co to znaczy… “ to, co zostało”?"

    bee "To, czego Nicość nie połknęła."
    bee "Jeszcze."
    bee "Wspomnienia… żale"
    bee "Resztki ludzi."

    "Pszczółka znów patrzy na Cotarda"

    bee "Albo resztki życia."
    bee "Prrrrrrrrrrrr"

    a "Przepraszam, że spytam ale…"
    a "Widziałaś może naszych rodziców?"
    a "Badaczy."
    a "Byli tu lata temu"


    bee "OoooooOOOo."
    bee "Tych."
    bee "Prrrrr."
    bee "Tak."
    bee "Widziałam."

    a "Co?! Naprawdę?!"
    a "Gdzie?!"
    a "Co się z nimi stało?!"

    "Pszczółka wykonuje kilka chaotycznych obrotów w powietrzu."
    bee "Pachniesz jak oni."
    bee "Zeszli niżej."
    bee "Niżej."
    bee "Niżej."
    bee "Zawsze niżej."
    bee "Szukali."
    bee "tak jak ty."

    bee "…"
    bee "Aleeee"
    bee "PRRRR"
    bee "Źródło patrzy też w górę."

    "Cotard patrzy na nią chłodno."
    c "Wiesz coś więcej o rodzicach?."

    "Pszczółka śmieje się."
    bee "Prr."
    bee "Czyli jednak ci zależy."
    bee "…"
    bee "Przeszli przez łąkę."
    bee "Kłócili się."
    bee "O to, które z nich zaczęło znikać pierwsze."

    "Cotard spogląda na Alyssie."
    "W jego oczach po raz pierwszy pojawia się cień napięcia."

    c "Kiedy?"

    bee "Tutaj?"
    bee "Tu czas nie istnieje."
    bee "Prr."
    bee "Ale dla Was?"
    bee "DAWNO."

    bee "Miło się gadało, lecę zapylać kwiatkiiiii!!!!"
    bee "Prrrrrrrrr!"

    "Pszczółka odlatuje i znika w oddali."

    "Alysia i Cotard stoją dłuższą chwilę w ciszy."
    "…"
    "Patrzą na siebie"
    "Alysia przerywa ciszę"
    "Zaciska notes przy piersi."

    a "Więc…"
    a "Naprawdę tu byli"

    "Cotard patrzy na nią."

    c "Albo to miejsce chce, żebyś w to uwierzyła."

    a "A jeśli choć raz nie masz racji?"

    c "…"

    "Nagle znów słychać bzyczenie"

    bee "Prrrrr!"
    bee "Jeśli chcecie znaleźć odpowiedzi…"
    bee "schodźcie niżej."
    bee "Ale uważajcie."
    bee "Na następnym poziomie Nicość nie pokazuje już kwiatów."
    bee "Pokazuje prawdę."
    bee "Czyli to, czego najbardziej się boicie."

    "Nie zdążyli zareagować."
    "Odleciała."

    "Z głębi łąki dobiega śmiech."

    "Dziecięcy."

    "Znajomy."

    "Alysia zamiera."

    unon "Pani Alysio!"

    "Na końcu ścieżki stoją dzieci."
    "Jej uczniowie."

    u "Wróci Pani?"
    u "Brakuje nam Pani…"

    "Cotard gwałtownie łapie ją za nadgarstek"
    "Jego dłoń jest lodowata."

    c "Nie patrz na nich!"

    a "To moi uczniowie!"
    a "Musieli się o mnie martwić!"

    "Alysia próbuje się wyrwać."
    "Cotard zaciska dłoń mocniej."

    a "{size=+20}Puść mnie Cotard!!!{/size}"

    "Pierwszy raz w jego głosie słychać… GNIEW."

    c "{size=+20}NIE.{/size}"
    c "{size=+20}to nie oni{/size}"
    c "{size=+20}NICOŚĆ wie, czego najbardziej ci brakuje.{/size}"
    c "{size=+20}I użyje tego przeciwko tobie.{/size}"

    "Głos."
    "Rozbrzmiewa wszędzie."

    unon "{size=+30}Jedno. Musi. Zniknąć.{/size}"

    "Alysia patrzy na Cotarda."
    a "Słyszysz to?"

    c "Tak."
    c "…"
    c "To nie głos."
    c "To brak czegoś, co powinno istnieć."

    n "Wszystko cichnie."
    n "Nawet kwiaty przestają drżeć."

    n "Przed nimi ziemia pęka na dwie ścieżki"
    n "Lewa - skąpana w jasnym miękkim świetle"
    n "Prawa - ciemna, pozbawiona koloru."
    nvl clear

    unon "{size=+30}Lewo - Zostań.{/size}" 

    unon "{size=+30}Prawo - Zejdź niżej. Ale stracisz.{/size}"

    unon "{size=+30}Alysio.{/size}"
    unon "{size=+30}Decyzja zależy od Ciebie.{/size}"

    "Zapada cisza."
    "Alysia patrzy na swoje dłonie."
    "Drżą."

    c "Alysio, musisz odpocząć."

    a "Ja…"
    a "Nie wiem, co mam zrobić,"
    a "Nie wiem, czy to w ogóle jest wybór."
    a "Ale czuję, że nie ma tu dobrej decyzji."
    a "Nie chcę ich stracić…"

    "Cotard patrzy na iluzje uczniów."
    "Na twarzy Alysii maluje się ból."

    a "Nie mogę."
    a "Nie mogę ich tak po prostu usunąć!"

    c "To nie oni!"

    a "Skąd wiesz?!!!"

    c "Bo Nicość nie daje."
    c "Ona tylko odbiera."
    c "Nie tworzy życia."

    a "A jeśli odbierze mi ich wspomnienia?!"

    c "Już zaczęła."
    c "Pamiętasz ich twarze?!"
    c "Pamiętasz jak wyglądała góra?!"

    "Alysia milknie."
    "Oczy jej drżą."
    "Próbuje sobie przypomnieć."
    "I nie potrafi."
    "To ją łamie."

    a "…"
    a "nie."

    c "No właśnie."

    a "Mówisz, że Oni nie istnieją…"
    a "To dlaczego o sobie mówisz to samo?"

    c "Jeśli tego nie usuniesz…"
    c "Nigdy stąd nie wyjdziesz."

    menu:
        "ZOSTAŃ":
            jump choice5chapter1_1
        "IDŹ DALEJ":
            jump choice5chapter1_2    

    label choice5chapter1_1:
    n "Alysia patrzy na swoich uczniów."
    n "Ich głosy są miękkie."
    n "Znajome."
    n "Pełne ciepła"
    n "Dotyka świetlistej chmury."
    n "W tej samej chwili świat mięknie."
    n "Kwiaty rozkwitają gwałtownie."
    n "Światło zalewa ekran"
    #dodać biały ekran
    n "Jej twarz rozluźnia się."
    n "Uśmiecha"
    nvl clear

    u "Gdzie pani była?"
    u "Martwiliśmy się."

    a "Ja…"
    a "chyba się zgubiłam."
    a "Ale już wszystko dobrze."
    a "Możemy wracać."

    n "Powoli siada na łące."
    n "Kładzie się między kwiatami."
    n "Oczy same się zamykają."

    n "Cotard rzuca się do Alysii"
    n "Po raz pierwszy jego głos"
    n "drży."
    nvl clear

    c "{size=+20}Alysia…{/size}"
    c "Nie…"
    c "Proszę…"
    c "Po jego policzku spływa łza."

    c "Nie zostawiaj mnie tutaj samego"
    c "…"
    c "Nie znikaj."

    n "Alysia nie odpowiada."
    n "Zostaje na łące."
    n "Uśpiona przez Nicość."
    nvl clear

    n "Cotard zaczyna płakać."
    nvl clear
    return

    label choice5chapter1_2:
    "Alysia zamyka oczy."
    "Łzy zbierają się pod powiekami."

    a "To nie oni."

    "Iluzja zaczyna pękać."
    "Światło przygasa."
    "Sylwetki uczniów powoli znikają"

    u "Pani Alysio… dlaczego…?"

    "Alysia odwraca wzrok"
    "Nie potrafi patrzeć."

    a "Przepraszam…"

    "Uczniowie znikają."
    "Zaczyna płakać"

    #dodać wyblakłą wersję bg
    "Świat wokół nich traci kolory."
    "Kwiaty stają się niemal szare."

    c "Dobrze"
    c "…"
    c "To jest prawdziwe."

    a "Co?"

    c "To, że ich nie ma"
    c "Wolałem się upewnić."
    c "… Chodź."
    c "Idziemy niżej"
    c "Alysia ociera łzy."

    a "Zaczynam rozumieć, dlaczego ludzie nie chcą wiedzieć."
    a "Jeśli każde zejście wymaga poświęcenia to…"
    a "ile z naszych wspomnień zostanie na końcu?"
    a "A jeśli na samym końcu nie zostanie nic?"
    a "to kim będę."
    jump Chapter_2



label Chapter_2:
    #dodać czarny ekran
    n "{size=+60}Rozdział Drugi{/size}"
    #Lodowa Nicość

    n "Powoli schodzą po schodach."
    n "Kamienna podłoga stopniowo przekształca się w lodową taflę pokrytą pajęczyną pęknięć."
    n "Wyczuwają pod stopami delikatny ruch. "
    nvl clear

    a "Cotard…"
    a "Zimno mi."
    a "Ale… Ale nie w ciało."
    a "Dziwne…"

    "Cotard patrzy na swoje dłonie."
    "Nie drżą."
    
    c "To nie jest zimno."
    c "To efekt Nicości."

    "Oddech Alysi staje się spokojniejszy."

    a "Czy to normalne, że przestaję się bać?"
    a "Przecież powinnam."
    a "Wiem o tym."
    a "Ale…"
    a "Jakby ktoś wyciszył mnie w środku."

    "Alysia dotyka klatki piersiowej."

    a "Jakby moje własne serce było gdzieś daleko stąd."
    a "Powinnam się bać…"
    a "A jakoś…"
    a "Nie potrafię."
    a "To chyba źle? Prawda?"

    "Cotard patrzy przed siebie."
    "Idzie nie zatrzymując się."
    "Milczy."

    "Docierają na sam dół schodów."
    scene bg ice cavern
    "Przed nimi rozpościera się niekończąca się jaskinia."

    c "Ten lód nie jest przezroczysty."
    c "Jest zapisany wspomnieniami."
    c "Tu byłem najniżej, nie wiem co jest dalej."

    n "Spod tafli lodu słychać szepty."
    n "Nie pojedyncze głosy."
    n "Dziesiątki. Setki."
    n "Nakładają się na siebie."
    n "Rezonują w narastający krzyk rozpaczy."
    nvl clear

    #SZEPTY:
    unon "…wróć…"
    unon "…nie pamiętasz mnie…"
    unon "…zostań…"
    unon "…to boli…"

    a "To są ludzie."
    a "To ich wspomnienia"

    c "Nie."
    c "To są resztki wspomnień, tych co byli w Nicości."

    n "Dwie ogromne bryły lodu z hukiem przebijają powierzchnię."
    n "Są idealnie gładkie."
    n "Ale ich wnętrze… Żyje."
    nvl clear

    n "{size=+20}Lewa Bryła:{/size}"
    n "Mały dom."
    n "Ciepłe światło."
    n "Śmiech."
    n "Mała Alysia ucieka z poduszką."
    n "Mały Cotard goni ją, wyraźnie zirytowany."
    nvl clear

    n "{size=+20}Prawa Bryła:{/size}"
    n "Stół."
    n "Rozłożona mapa Nicości."
    n "Rodzice kłócą się."
    n "Atmosfera napięta."
    n "Strach."
    nvl clear

    a "To… my."
    a "To naprawdę my."

    c "Wydaje mi się, że to zapis tego co było."
    c "Albo tego, co Nicość chcę żebyś pamiętała."

    "Alysia wyciąga rękę."
    "Dotyka lodu."
    "Nic."
    "Patrzy na Cotarda."

    a "Musimy razem."
    a "Prawda?"

    "Cotard przez chwile się nie rusza."
    "Potem przykłada dłoń"

    #WYBÓR 
    menu:
        "DZIECIŃSTWO":
            jump choice1chapter2_1
        "RODZICE":
            jump choice1chapter2_2

    label choice1chapter2_1:
        #dodać czarne tło
    n "Lód pęka"
    n "Świat zmienia się natychmiast."
    n "Ciepło."
    n "Zapach drewna."
    n "Światło ognia."
    nvl clear

    #<Czarne tło> -potencjalnie dodać jakieś fajne fullarty

    la "Oddaj! To moja poduszka!"

    lc "Nie jest twoja!"
    lc "Zabrałaś mi ją pierwsza."

    "Cotard rzuca poduszką w Alysie."
    "Alysia piszczy i śmieje się."

    lc "Przestań się śmiać!"
    lc "To nie jest śmieszne!"

    "Alysia rzuca kolejną poduszką."
    "Trafia go."
    "Cotard się zatrzymuje"
    "Przez sekundę wygląda jakby miał się rozpłakać."
    "Ale zamiast tego…"
    "Rzuca książką."

    #<Koniec czarnego tła>

    a "To był ten moment…"
    a "Siniak."
    a "Ukrywaliśmy to przed rodzicami."
    a "Bałam się, że zamkną biuro."

    c "Bałaś się bardziej kary, czy tego, że stracisz dostęp do wiedzy?"

    "Alysia patrzy na niego zaskoczona"

    a "…" 
    a "obu."

    c "To nie było całe wspomnienie."
    c "Tylko fragment."

    a "…"
    jump choice1chapter2_done

    label choice1chapter2_2:
        #dodać czarne tło
    n "Lód pęka."
    n "Zimno uderza natychmiast."
    n "Stół."
    n "Mapa Nicości."
    n "Zaznaczone poziomy."
    n "Niektóre przekreślone."
    nvl clear
    #<Czarne tło> -potencjalnie dodać jakieś fajne fullarty

    f "To nie jest tylko struktura!"
    f "To system!"

    m "System?!"
    m "Czego?!"
    m "Znikania?!"

    f "Każdy poziom coś zabiera!"
    f "Najpierw zmysły!"
    f "Potem pamięć!"
    f "Potem…"

    #<Koniec czarnego tła>
    #<Czarne tło> -potencjalnie dodać jakieś fajne fullarty

    m "A jeśli to miejsce nie odbiera…"
    m "tylko odsłania?"

    #<Koniec czarnego tła>

    a "Oni wiedzieli…"
    a "więcej niż mówili…"

    c "Dobrze wiedzieli, co ich czeka."
    jump choice1chapter2_done

    label choice1chapter2_done:
    n "Obydwie bryły lodu zostały zniszczone."
    n "Na ich miejscu pojawiły się jedna, nowa."
    nvl clear
    #czarne tło
    n "Sala."
    n "Dziesiątki ludzi."
    n "Zatrzymani w ruchu."
    nvl clear

    n "Cotard i Alysia dotykają razem bryłę lodu."
    n "Lód pęka."
    nvl clear

    #<Czarne tło> -potencjalnie dodać jakieś fajne fullarty
    m1 "To nie jest teoria."
    m1 "Mamy dowód."

    k1 "Nie powinniśmy byli go sprowadzac z powrotem."

    om "Musieliśmy."
    om "To jedyna osoba, która wróciła."

    m2 "To NIE jest osoba."

    k2 "Nie ma reakcji emocjonalnych."
    k2 "Nie reaguje na bodźce."
    k2 "Nie rozpoznaje części własnych wspomnień."

    m1 "Twierdzi, że nie istnieje."

    k2 "To klasyczny rozpad tożsamości."

    om "Nie."

    "Wszyscy milkną"

    om "To adaptacja."


    m2 "Adaptacja?!"
    m2 "Czego?!"

    om "Milczeć!"
    om "Spełnił to czego Nicość wymaga"
    om "Stracił emocje."
    om "Stracił poczucie istnienia."
    om "Ale dzięki temu…"
    om "Przetrwał."

    om "Musimy wysłać kogoś głębiej."

    #<Koniec czarnego tła>

    "Bryła się nie rozpadła, jest zmieniona."


    "Dotykają jej ponownie."

    #<Czarne tło> -potencjalnie dodać jakieś fajne fullarty

    "Na ziemi leży blade, rozkładające się ciało."

    "To Cotard."

    #<Koniec czarnego tła>

    c "To ten moment,"
    c "w którym przestałem istnieć."

    a "Nie możesz tak mówić!"
    a "Przecież stoisz tutaj!"
    a "Oddychasz!!!"

    c "Nie."
    c "To co widzisz…"
    c "To kontynuacja mojej śmierci."
    c "Po tym… "
    c "Nagle znów mogłem się ruszać…"

    a "Jeśli to wspomnienie jest prawdziwe…to kim jesteś?"

    "Cotard patrzy na nią bez emocji."

    #<Czarne tło> -potencjalnie dodać jakieś fajne fullarty

    "Cotard jest w sali narad."

    m1 "…"
    m1 "on nie oddycha."

    k1 "Nie ma pulsu"

    m2 "Więc o czym my w ogóle rozmawiamy?"
    m2 "To ciało."

    om "Milcz."

    om "Notuj."
    om "Brak reakcji na bodźce."
    om "Brak funkcji życiowych."

    "Nagle palec martwego Cotarda drga."

    k1 "Widzieliście to?!"

    "Martwy Cotard otwiera oczy."

    "Nie łapie oddechu."
    "Nie reaguje."
    "Nie porusza się gwałtownie."

    "Po prostu…"
    "Patrzy."

    m1 "…czy on nas widzi?"

    "Cotard powoli podnosi głowę."
    "Siada."

    c "…"
    c "to nie ma znaczenia."

    k1 "On… mówi"

    m2 "Nie."
    m2 "Nie, nie nie…"

    om "Cisza!"

    "Starszy mężczyzna podchodzi do Cotarda."
    "Patrzy mu prosto w oczy."

    om "Jak się nazywasz?"

    c "To nie ma znaczenia."

    om "To dziecko spełniło warunek."
    om "Oddał wszystko, co było zbędne."

    om "Musimy spróbować ponownie."
    om "Zobaczyć co się stanie."

    k1 "Oszalałeś?!"

    om "Musimy, inaczej nie dowiemy się dlaczego."


    #<Koniec czarnego tła>

    c "Ja tego nie pamiętam."
    c "Nie wiem kim są ci ludzie."

    a "Oni… patrzyli na Ciebie jak na narzędzie."
    a "Mówili o tobie jak o wyniku."
    a "Nie jak o człowieku."

    c "Bo człowiekiem przestałem być dla nich w momencie, kiedy przestałem reagować."
    c "Dla siebie również."

    a "Pamiętasz swoje pierwsze zejście do Nicości?"

    c "Nie."

    a "Dlaczego tam chodziłeś, jak już stałeś się sobą?"

    c "Bo ja nie wiem, co tracę."
    c "Więc nie mam czego żałować."

    n "Hałas wokół nich milknie,"
    n "Żadnych szeptów."
    n "Żadnych ruchów."

    n "Jakby wszystko…"
    n "Zostało już zapisane"
    n "i zamknięte."
    nvl clear

    a "Cotard…"
    a "Co się teraz stanie?"

    "Nie odpowiada od razu."

    c "…"
    c "Myślę, że to moment…"
    c "W którym jesteśmy sprawdzani."

    n "Lód pod ich stopami zaczyna drżeć."
    n "Nie pęka."
    n "Nie rozpada się."
    nvl clear

    unon "{size=+30}Wystarczająco. Oddaliście.{/size}"

    a "Nie chcieliśmy niczego oddawać."

    unon "{size=+30}Nicość{/size}"
    unon "{size=+30}Nie ma różnicy.{/size}"

    "Te słowa…"
    "Uderzają mocniej niż powinny."

    "Cotard stoi spokojnie"
    "Jakby wszystko było logiczne"

    "Lód przed nimi topi się, a rozgrzana woda paruje."
    "Pojawia się tunel do wnętrza wodnej czeluści."

    unon "{size=+30}Możecie zejść niżej.{/size}"

    a "Ile jeszcze…"

    unon "{size=+30}Tyle ile pozostało.{/size}"

    "Ruszają"

    n "Lód zamyka się nad nimi."
    n "Cisza wraca."
    n "Jakby nic nigdy się tu nie wydarzyło."
    nvl clear

    #KONIEC ROZDZIAŁU 2
label chapter_3: 
    #czarne tło
    n "{b}{size=+60}Rozdział 3{/size}{/b}"
    n "Schodzą."
    n "Długo."
    n "Za długo."
    n "Lód znika."
    n "Nie pęka."
    n "Nie topnieje."
    n "Po prostu… przestaje istnieć."
    n "Pod nimi:"
    n "ciemność."
    n "A potem"
    n "woda."
    n "Ale nie taka jak na powierzchni."
    n "Nie ma fal."
    n "Nie ma dźwięku."
    n "Nie ma oporu."
    n "Wygląda jak ocean."
    n "Ale nie zachowuje się jak ocean."
    n "…"
    n "Alysia robi krok."
    n "Ale... zatrzymuje się."
    nvl clear


    a "…Cotard."
    "Dotyka powierzchni wody."

    "Nie rozlewa się."
    "Nie reaguje."

    a "To nie jest woda. "
    a "Jest jak powietrze."

    "Alysia bierze głęboki oddech."

    a "Musimy…?" 

    c "Tak."
    "Robią krok."
    "Zapadają się w wodę."
    scene bg void sea

    n "Nie ma szoku."
    n "Nie ma duszenia się."
    n "Jest tylko—"
    n "cisza."
    nvl clear
    "Alysia otwiera oczy. "
    "Widoczność jest dziwna."
    "Nie ma światła."
    "A jednak widzi."
    "Porusza ręką. "
    "Jej ruch jest wolniejszy."
    "Ale… naturalny."

    a "Ja…" 
    "Alysia próbuje oddychać."
    "Nic. "
    "..."
    #Panika
    #- ale tylko przez sekundę.

    a "{size=-10}Mogę oddychać, ale nie w pełni.{/size}"

    "Cotard patrzy na nią."

    c "Zobaczymy co będzie dalej."

    "W oddali"
    "coś się porusza."
    "Organiczna forma życia"
    "płynie w ich stronę."
    "Wygląda jak niebieska ośmiornica."
    "Jej ciało pluska miękkim światłem"
    "Gdy zbliża się, słychać szept"
    "Nie słów a uczuć."

    "Czuć ciepło, spokój, zgodę."

    "Alysia wyciąga rękę"

    c "{size=+20}Nie!{/size}"

    "Za późno."
    "Alysia dotyka jednej macki."
    "Ośmiornica przykleja się do jej dłoni."
    "A potem"
    "przesuwa się wyżej"
    "na szyje"
    "Alysia zastyga."

    a "Cotard…" 

    n "Meduza delikatnie „otwiera się” przy jej gardle."
    n "Wnika w nią."
    nvl clear

    "Alysia bierze oddech. "
    "Głęboki, spokojny"
    #Alysia (zaskoczona):
    a "…czuje się lekko, łatwiej mi oddychać."
    "Cotard patrzy."
    "Nie rusza się."

    c "Adaptujesz się do tego."
    c "Ale koszt tego jeszcze nie przyszedł."

    #WYBÓR 1  MEDUZA
    menu:
        "Dotykasz meduzy":
            jump choice1chapter3_1
        "Odsuwasz się":
            jump choice1chapter3_2
    #OPCJA 1 — ADAPTACJA
    label choice1chapter3_1:
    "Cotard w końcu sięga ręką."
    "Dotyka meduzy."
    "Meduza przywiera do jego dłoni."
    "Ale nic się nie zmienia."

    a "Co czujesz?" 

    c "Nic nowego. "
    c "Ale działa - łatwiej mi oddychać."
    jump choice1chapter3_done

    #OPCJA 2 OPÓR
    label choice1chapter3_2:
    "Cotard odsuwa się."
    "Próbuje oddychać. "
    "Sekundy mijają. "
    "Alysia patrzy na niego z niepokojem."

    a "Cotard… "

    "Jego ruchy zwalniają." 

    "W końcu"
    "łapie meduzę."
    "Pozwala jej się przyczepić." 

    c "To nie było opcjonalne."
    jump choice1chapter3_done

    label choice1chapter3_done:
    "Alysia nie już patrzy na niego."
    "Patrzy w dół. "
    "Coś leży na dnie. "

    c "Widzę."
    c "Zbliżają się. "
    c "To nie jest część oceanu. "
    c "To coś obcego."
    n "Metal."
    n "Zardzewiały."
    n "Ale nie zniszczony."
    n "Częściowo wbity w „dno”, które nie jest dnem."
    n "Alysia przyspiesza."
    nvl clear
    a "{size=-10}Nie… {/size}"

    "Podpływa bliżej." 

    "Zbliża swoją dłoń do przedmiotu"
    "Ale jej dłoń zatrzymuje się"
    "Drży."

    a "To…" 

    "Dotyka przedmiotu"
    "Obraca powoli kawałek metalu."
    "Na powierzchni widać wyryty znak." 
    "Znajomy"

    a "{size=-10}…to narzędzie ojca.{/size}"

    "Cotard patrzy. "
    "Nie reaguje emocjonalne, ale od razu widać po nim, że analizuje całą sytuację."
    "W ostatniej chwili powstrzymuje się."

    c "Jesteś pewna? "
    c "Alysia kiwa głową. "

    a "On zawsze znakował sprzęt."
    a "Żeby go nie zgubić w terenie."

    "Przesuwa palcem po znaku." 


    a "To jego." 

    c "Nie jestem tego pewien."

    a "Dlaczego?" 

    c "Bo to poziom niżej niż ten, na którym ja byłem."
    "Alysia zaczyna rozglądać się nerwowo." 
    
    a "Jeśli to tu jest… to musi być więcej."
    "W oddali"
    "coś świeci."
    "Podpływają. "
    "To fragment materiału. "
    "Część ubrania."
    "Znów znajomy. "
    "Alysia dotyka go. "
    #TU BĘDZIE WIZJA TAKI FLASHBACK CZY COŚ BOOM
    n "Matka. "
    n "Oddycha ciężko. "
    n "Patrzy w dół. "
    nvl clear
    m "…jeszcze niżej…" 
    "Obraz się urywa." 

    a "Oni… schodzili dalej." 

    c "Świadomie." 

    a "Jeśli oni zeszli niżej niż ty…" 

    a "…to znaczy, że istnieje coś jeszcze." 

    c "Zawsze istnieje coś jeszcze." 

    c "Pytanie brzmi… "
    c "…czy powinniśmy to zobaczyć." 


    n "Płyną dalej. "
    n "Ich ciała zaczynają się zmieniać."
    n "Skóra Alyssii:"
    n "delikatnie przezroczysta."
    n "Jej ruchy:"
    n "bardziej płynne."
    n "Jej oddech:"
    n "zbyt spokojny"
    nvl clear

    a "To… nie boli."
    a "Powinno?"

    c "Nie wszystko tutaj boli."
    #WYBÓR 2  ZMIANY CIAŁA
    menu:
        "Akceptujesz zmiany":
            jump choice2chapter3_1
        "Próbujesz się im opierać":
            jump choice2chapter3_2

    #OPCJA 1  AKCEPTACJA
    label choice2chapter3_1:

    "Alysia zamyka oczy."

    a "Jeśli to pozwala nam iść dalej…" 

    "Oddycha głębiej." 

    "Zmiany przyspieszają." 

    a "To… nawet przyjemne." 
    jump choice2chapter3_done

    #OPCJA 2  OPÓR
    label choice2chapter3_2:

    "Alysia próbuje zdjąć meduzę."

    "Nie da się."
    "Im bardziej próbuje"
    "tym bardziej się wtapia."

    a "Nie chcę tego!" 
    "Jej ruchy stają się chaotyczne."
    "Na chwilę traci kontrolę nad oddechem."
    "Cotard łapie ją. "

    c "Przestań." 
    jump choice2chapter3_done

    label choice2chapter3_done:
    n "Ocean zmienia się. "
    n "Nie ma już kierunku."
    n "Nie ma góry."
    n "Nie ma dołu."
    n "Alysia patrzy wokół. "
    nvl clear

    a "Cotard… "
    a "Nie chcę iść dalej. "

    c "Dlaczego?" 

    a "Bo tutaj… wszystko jest prostsze. "
    a "Nie boli."

    #WYBÓR 3  PRZYWIĄZANIE DO POWIERZCHNI
    menu:
        "Chce iść dalej.":
            jump choice3chapter3_1
        "Chce zostać.":
            jump choice3chapter3_2

    #OPCJA 1  TRZYMANIE SIĘ
    label choice3chapter3_1:

    a "Nie."
    a "To zły pomysł."
    a "Musimy iść."
    a "Mamy powód."
    a "Mamy siebie. "
    jump choice3chapter3_done

    #OPCJA 2  ODPUSZCZENIE
    label choice3chapter3_2:

    "Alysia uśmiecha się lekko."

    a "A po co? "
    a "Po co iść dalej"
    a "Tam… wszystko boli"

    "Dotyka wody."

    a "Tutaj… nie."

    "Cotard patrzy na nią długo. "

    c "To nie jest brak bólu. "
    c "Tracisz kawałki siebie."
    c "Przestajesz się czuć sobą."
    jump choice3chapter3_done

    #DECYZJA GŁÓWNA 
    label choice3chapter3_done:
    n "Ocean zatrzymuje się. "
    n "Wszystko zamiera. "
    n "Ośmiornica zaczyna bardzo mocno świecić"
    nvl clear


    unon "{size=+30}Wybierz.{/size}" 
    n "Dwie przestrzenie otwierają się przed nimi." 

    n "Jedna:"
    n "ciemniejsza."
    n "cięższa."
    n "Druga:"
    n "lekka."
    n "spokojna."
    nvl clear

    menu:
        "Usuń ból.":
            jump choice4chapter3_1
        "Lub usuń uczucia.": 
            jump choice4chapter3_2

    #WYBÓR KOŃCOWY
    label choice4chapter3_1:
    
    n "Alysia zamyka oczy."
    nvl clear

    a "Nie chcę już cierpieć."
    n "Świat cichnie."
    n "Wszystko staje się…"
    n "spokojne."
    n "Ale"
    n "Jej oczy pustoszeją"
    n "Patrzy na Cotarda."
    nvl clear

    a "…kim jesteś?" 
    "Cotard patrzy na nią. "
    "Cisza."
    jump choice4chapter3_done

    label choice4chapter3_2:
    n "Alysia patrzy na Cotarda."
    n "Długo. "
    nvl clear

    a "Przepraszam."
    "Uśmiecha się."

    "Ostatni raz."

    a "To nie ma sensu trzymać się czegoś, co i tak zniknie."
    a "Teraz będziemy podobni do siebie."

    n "Jej wyraz twarzy mięknie. "
    n "emocje znikają."
    n "Patrzy na niego spokojnie." 

    n "Bez miłości"

    n "Bez uśmiechu"
    nvl clear

    a "Możemy iść dalej." 


    #KONIEC ROZDZIAŁU
    label choice4chapter3_done:
    n "Ocean otwiera się. "
    n "Droga prowadzi niżej."
    n "Jeszcze głębiej."
    n "Zanurzają się dalej. "
    n "Bez oporu. "

    n "Ośmiornica odkleja się od nich"
    n "Jej światło gaśnie."

    n "Alysia nagle próbuje nabrać powietrza"
    n "i tym razem"
    n "czuje opór."
    nvl clear

    #Alysia (gwałtownie):
    a "Nie mogę…"

    n "Ale zamiast ich topić…"
 
    n "woda znika. "

    n "Nie odpływa."
    n "Nie opada."
    n "przestaje istnieć. "
    n "Upadają. "
    n "Zatrzymują się w pół ruchu. "
    n "Jakby coś ich trzymało. "
    n "A potem "
    n "grunt. "
    n "Twardy."
    n "Wilgotny."
    n "Ciemność. "
    nvl clear

    n "{size=+40}KONIEC ROZDZIAŁU 3{/size}"

    return
