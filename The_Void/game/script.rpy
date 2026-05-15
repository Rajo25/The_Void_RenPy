# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define narrator = nvl_narrator
define a = Character("Alisia", color="#fffd7b")
define c = Character("Cotard", color="#9c1908")
define bee = Character("Przczułka", color = "#ffa600")
define unon = Character("???", color = "#ffffff")
define u = Character("Uczniowie", color = "#a1fd28")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg mountain.png" or "bg mountain.jpg") to the
    # images directory to show it.

    scene bg mountain

    # These display lines of dialogue.
    "Jestem osobą, która pyta.{w=1}\ Nie potrafię inaczej, nigdy nie potrafiłam."
    "Pytam o wszystko, jakby ktoś zapisał we mnie wewnętrzny przymus aby zrozumieć niezrozumiałe."
    "Pociąga mnie to co jeszcze nienazwane, niewypowiedziane, o których inni boją się nawet pomyśleć."


    "Dratoc pojawił się w naszym życiu niespodziewanie."
    "Pewnego dnia rodzice po prostu przyszli z nim do domu, i tak już zostało."
    "Znaleźli go na wybrzeżu, gdzie spacerowali."
    "Nigdy nie dowiedziałam się kto go tam porzucił i dlaczego."
    "Ale to nieważne."
    "Liczyło się dla mnie tylko to, że został."
    "Dołączył do naszej rodziny jako jej pełnoprawna część."

    "Nie rozumiem tego, co wydarzyło się później.{w=1}\ Przecież było idealnie."
    "Ale wtedy rodzice postanowili wyruszyć w Nicość."
    "Bez wyjaśnień i bez pożegnań.{w=1}\ Poszli tam, gdzie nikt się nie zapuszcza."
    "Po co?"
    "W końcu jeszcze nikt stamtąd nie wrócił."

    "To wydarzenie strzaskało moją potrzebę rozumienia wszystkiego."
    "Oto bowiem stało się coś, czego zrozumieć nie mogłam i nadal nie mogę."

    "Może to okrutne, ale uważam, że moi rodzice nigdy nie myśleli trzeźwo."
    "Choć jestem im za to wdzięczna, zabrali do domu obce dziecko i potraktowali jak własne."
    "Kto normalny tak robi?!"

    "Zawsze wszystko robili po swojemu."
    "Nasze wychowanie nie odbiegało od dziwnego schematu, w którym postanowili uczyć nas samodzielnie w domu zamiast posłać do szkoły."
    "Gdy skończyłam cztery wiosny uczyli nas zielarstwa i podstawowej pierwszej pomocy."
    "Gdy skończyłam szóstą wiosnę umiałam już polować i przyrządzać zwierzęta."

    "Na Górze nie miałam nikogo, rodzice przypłynęli tu z kontynentu."
    "Zostaliśmy więc zupełnie sami."
    "Wylądowaliśmy w sierocińcu."
    "Było to dobre i bezpieczne miejsce, a nasi opiekunowie pełni pasji i miłości do dzieci."
    "Ale nie byli NIMI."
    "Samotność i poczucie opuszczenia pożerały nas od środka."
    "Dobrze, że mieliśmy choć siebie."

    "Już dosyć wcześnie interesowałam się pracą społeczną i pomaganiem innym."
    "Zaczęłam się przyglądać, a potem uczestniczyć w opiece nad innymi dziećmi."
    "Stopniowo dochodziłam do siebie."
    "Dorastając znów czułam pociąg do zdobywania wiedzy, by potem dzielić się nią z innymi."
    "Było więc oczywiste, że zostanę nauczycielką."

    "Wiedza jest bezcenna - bo pozwala oswoić strach."

    "Zaś co do Dratoca…"
    "Zniknięcie rodziców zmieniło go."
    "Nie zauważyłam tego od razu."
    "Coś w nim pękło."
    "Z czasem ta szczelina rosła i rosła, aż pochłonęła go w całości."
    "Zamykał się w sobie, odcinał."
    "Przeraziło mnie, gdy pewnego dnia stwierdził, że nie ma go już."
    "Że nie istnieje."

    "Oświadczył też, że przestał być Dratocem, a zaczął…"
    "Cotardem."
    "Reagował wyłącznie na swoje nowe imię."
    "Próbowałam walczyć, ale co mogłam zrobić?"
    "Mogłam się z nim porozumieć tylko wtedy, gdy ulegałam i zwracałam się do niego tak, jak chciał."
    "Inni o dziwo nie zwracali uwagi."
    "Nie obchodziło to ich tak, jak mnie."

    "Stał się chłodny. Cichy."
    "Nie był już dzieckiem, które poznałam i uznałam za swojego małego braciszka."
    "Dawniej potrafił gadać bez końca, topił mnie w potoku słów."
    "Ale już nie."
    "Odzywa się tylko wtedy, gdy uzna to za konieczne."
    "Czyli prawie nigdy."

    "Ale wciąż uważam go za mojego brata."
    "Zawsze będę. Kocham go całym sercem."

    "To postępuje."
    "Zmuszam go do posiłków, sam najchętniej nic by nie jadł."
    "Twierdzi, że nie potrzebuje jedzenia."
    "Tylko moje łzy i błagania skutkują."
    "Choć do straszne, znajduję w tym pocieszenie - oznacza bowiem, że mój brat nadal czuje emocje. Nadal mu zależy."
    "To dla mnie znaczy wszystko."

    "Ubrania zużywają się na nim jak drewno w ognisku."
    "Wrzucam je potajemnie, żeby nie zobaczył zaschniętych śladów krwi i oderwanych kawałków skóry."
    "Przeraża mnie to."
    "Cotard ropieje, jego skóra pęka, pokrywa się pęcherzami i liszajem."
    "Nie mówi mi skąd się to bierze."
    "Ale ja wiem."

    "Kiedy próbuje zdecynferkować jego rany, on spokojnie odmawia."
    "Mówi, że tego nie potrzebuje."
    "Tutaj mój płacz nie pomaga."
    "NIC nie pomaga."
    "NIC."

    "Nigdy nie chodzi z nami do gorących źródeł."
    "Pytałam, czy chodzi o rany, ale stwierdził, że nie."
    "Po prostu nie chce."
    "Myśli, że nie widzę jego reakcji na wodę."
    "Unika jej jak trucizny. "
    "Nie myje się."
    "Cichnie chorobą, ale o dziwo nie jest chory."
    "O co w tym chodzi…"

    "Pije tylko grzybowy napar. Dobrze, że chociaż tyle."

    "Wiem już na pewno, ale nikomu nie powiem."
    "On chodzi do Nicości."
    "Jest jedynym, który w Niej był i wrócił."
    "Próbowałam go o to pytać, ale udaje, że nie słyszy."
    "Zamyka się zupełnie i mnie odcina,"
    "Nie zaprzecza."
    "Po prostu stawia przede mną mur."

    "Praca w prosektorium mu pomaga."
    "Mało kto go tam ogląda, a sam Cotard dobrze się czuje wśród zmarłych."
    "Zupełnie, jakby był jednym z nich."

    "Dopiero po czasie zrozumiałam, że Cotard nie ma węchu."
    "Do domu wraca uśmiechnięty, zadowolony."
    "Zamyka się w szopie i siedzi w niej do następnego dnia."
    "Rano idzie do pracy. I tak dzień w dzień."

    "Nieraz próbowałam się włamać do jego kryjówki, ale nic z tego."
    "Kłódka jest mocna, a łańcuchy dobrej jakości. Drzwi mocne."
    "Z wnętrza dobiega dziwny jęk."
    "Boję się."

    "Ludzie dziwnie na nas patrzą."
    "Gdyby tylko umieli w nim dostrzec, co ja…"

    "Wczoraj spytałam go co robi w tej swojej szopie"
    "Powiedziałam, że chcę wiedzieć BO MAM PRAWO."
    "Uśmiechnął się tylko i odparł, że to niespodzianka."
    "NIESPODZIANKA?"
    "Ile lat to już trwa"
    "PO CO?"
    "DLA KOGO?"
    "Pogłaskał mnie po głowie mówiąc: “Już niedługo siostrzyczko. Zobaczysz. Już niedługo”"
    "Zaczęłam płakać."
    nvl clear

label Chapter_1:

    scene bg void entrance

    "{size=+20}Dziennik Alysii Wpis 001{/size}"

    "Dla moich uczniów"

    "Jeśli czytacie te słowa, to wiecie już, że jestem w miejscu, do którego nikt nie powinien wchodzić."
    "On… mówił mi, żebym tego nie robiła."
    "Że nie wszystko jest do odkrycia."
    "Że niektóre tajemnice istnieją tylko po to, by pozostać tajemnicami."

    "Ale jeśli świat ma sens, to musi istnieć jego źródło."

    "A jeśli go nie ma…
    …to chcę wiedzieć dlaczego."

    "Nie idę tam jako bohaterka."
    "Idę jako nauczycielka, która nie potrafi znieść niewiedzy."

    "Chcę wiedzieć, co się stało z moimi rodzicami."

    "I nie jestem sama."
    "Nie martwcie się."
    "{b}On się mną zaopiekuje.{/b}"
    nvl clear
    "{b}{size=+60}Akt Pierwszy{/size}{/b}"
    nvl clear
    "Wiatr… jest dziwnie cichy"
    "Nie zimny. Nie ciepły."
    "Po prostu… czuć, że pochodzi z Nicości."
    
    "Ogromny krater ciągnie się w dół, jakby świat został wyrwany z własnego ciała."
    
    "Alysia staje na krawędzi."
    "A obok niej "
    "Cotard."
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

    "Powietrze robi się słodkie."
    "Zbyt słodkie."
    "Duszące."
    "W oddali zaczynają się wyłaniać pierwsze kwiaty."
    "Delikatne."
    "Białe."
    "Ich płatki poruszają się mimo, że nie ma wiatru"

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

    "{size=+20}Dziennik Alysii Wpis 002{/size}"

    "Kwiaty."
    "Nie potrafię opisać ich piękna."
    "Są zbyt doskonałe."
    "A przez to nienaturalne."

    "Cotard twierdzi, że nie są prawdziwe."
    "I co najgorsze…"

    "wierzę mu."

    "Mam jednak dziwne wrażenie, że to miejsce reaguje na emocje."
    "Na zachwyt."
    "Na lęk."
    "Na wspomnienia."

    "Im bardziej chcę coś zrozumieć, tym bardziej rzeczywistość wydaje się miękka."
    "Jakby można ją było rozerwać palcami."

    nvl clear

    "Kwiaty drżą."
    "Pył unosi się w powietrzu jak złoty dym."
    "Z głębi łąki dobiega dźwięk."
    "Coś bardziej pomiędzy śmiechem a buczeniem"
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
    nvl clear
    "…"
    nvl clear
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

    "Wszystko cichnie."
    "Nawet kwiaty przestają drżeć."

    "Przed nimi ziemia pęka na dwie ścieżki"
    "Lewa - skąpana w jasnym miękkim świetle"
    "Prawa - ciemna, pozbawiona koloru."

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
    "Alysia patrzy na swoich uczniów."
    "Ich głosy są miękkie."
    "Znajome."
    "Pełne ciepła"
    "Dotyka świetlistej chmury."
    "W tej samej chwili świat mięknie."
    "Kwiaty rozkwitają gwałtownie."
    "Światło zalewa ekran"
    "Jej twarz rozluźnia się."
    "Uśmiecha"

    u "Gdzie pani była?"
    u "Martwiliśmy się."

    a "Ja…"
    a "chyba się zgubiłam."
    a "Ale już wszystko dobrze."
    a "Możemy wracać."

    "Powoli siada na łące."
    "Kładzie się między kwiatami."
    "Oczy same się zamykają."

    "Cotard rzuca się do Alysii"
    "Po raz pierwszy jego głos"
    "drży."

    c "{size=+20}Alysia…{/size}"
    c "Nie…"
    c "Proszę…"
    c "Po jego policzku spływa łza."

    c "Nie zostawiaj mnie tutaj samego"
    c "…"
    c "Nie znikaj."

    "Alysia nie odpowiada."
    "Zostaje na łące."
    "Uśpiona przez Nicość."
    nvl clear

    "Cotard zaczyna płakać."
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


    "tu zaczyna się akt 2"
    # This ends the game.

    return
