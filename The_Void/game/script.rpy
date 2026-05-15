# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define narrator = nvl_narrator
define a = Character("Alisia", color="#fffd7b")
define c = Character("Cotard", color="#fffd7b")


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

    "Dziennik Alysii Wpis 001"

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
    "{b}{size=+60}Wejście do Nicości{/size}{/b}"
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

    Alysia:
    Właśnie dlatego tu jesteśmy.


    Cotard patrzy w dół.
    Długo.
    Zbyt długo.

    Cotard:
    Nie czuję strachu.
    …
    To nie jest odwaga.

    #Alysia:
    #1> Wiem, to głupota.
    #2> Dlaczego tak mówisz?

    #Cotard:
    #1> To dobrze.
    #Przynajmniej to się nie zmieniło
    #2> Bo ja i tak nie istnieję.
    #A jednak nadal potrafię popełniać błędy.

    Zejście
    Pierwszy krok.
    Ziemia nie wydaje dźwięku.

    Alysia:
    Słyszysz to?

    Cotard:
    Nie
    …i właśnie to powinno cię martwić.

    Alysia:
    Jesteś jedyną osobą, która może tam wejść i wrócić.

    Cotard przekrzywia głowę jakby analizował coś czego nie da się zrozumieć

    Cotard:
    Boje się, jak na Ciebie zadziała to otoczenie.

    #Alysia:
    #1> Też się martwię
    #2> Przekonamy się.
    #OPCJA 1
    #Alysia:
    #Też się martwię.
    #Boję się, że nagle coś się zmieni i Nicość zacznie działać również na ciebie.
    #Że odbierze mi nawet tę pewność, którą teraz mam.
    #Ale… przekonamy się, gdy dojdziemy do Kwiecistej Nicości.

    #Cotard patrzy na nią długo.
    #Jego twarz pozostaje niemal nieruchoma, ale głos staje się cichszy.


    #Cotard:
    #…
    #Nie martw się o mnie.
    #Na mnie już Nicość wypróbowała wszystko, co mogła.
    #…


    #Alysia:
    #Nieprawda.
    #Gdyby zrobiła wszystko, nie szedłbyś teraz obok mnie.

    #Cotard milknie.
    #Jakby nie potrafił znaleźć odpowiedzi.
    #Po chwili rusza dalej.

    #Cotard:
    #…to nie jest argument.

    #Alysia lekko się uśmiecha.
    #Alysia: 
    #Jest.

    #OPCJA 2
    #Alysia:
    #Przekonamy się z czasem.
    #Mam nadzieję, że po prostu nic nam się nie stanie
    #Może to miejsce tylko tylko próbuje nas przestraszyć.

    #Spogląda w nicość

    #Cotard:
    #Dziwne.
    #Ludzie zawsze próbują nadać sens temu, czego się boją.
    #Jakby nazwanie lęku czyniło go mniejszym.

    #Alysia:
    #A ty?
    #Na czym budujesz strój spokój

    #Cotard:
    #Na pustce.
    #Nie oczekuję już niczego dobrego.

    #Alysia:
    #A ja właśnie odwrotnie.
    #Oczekuje, że damy sobie radę.
    #Dlatego dobrze, że idziemy razem.



    #JAKIEŚ PÓŁ H ZEJŚCIA


    Cotard:
    Nie odwracaj się.
    Już tego nie ma.

    Alysia:
    Czego?

    Cotard:
    Góry.
    Zapomniałem jak wyglądała.

    #Alysia:
    #1> Co?! To się dzieje za szybko…
    #2> Zauważyłam już… i to mnie przeraża.


    #Cotard:
    #1> Nie przesadzaj
    #To normalne.
    #2> To normalne.
    #Przyzwyczaisz się.

    Po tych słowach Cotard rusza dalej.
    Jego kroki są ciche.
    Nie dlatego, że stawia je lekko,
    Po prostu Nicość nie oddaje dźwięku
    Alysia idzie tuż za nim
    Im niżej schodzą, tym bardziej powietrze staje się…
    inne
    Nie cięższe.
    Nie rzadsze.
    Po prostu obce.
    Jakby nie należało do świata.

    Alysia:
    Cotard…
    Czy to tylko mi sie wydaje, czy powietrze tutaj pachnie inaczej?

    Cotard zatrzymuje się na moment 
    Unosi głowę.


    Cotard:
    Tak.
    Wszystko zaczyna się tutaj.

    Alysia:
    Co takiego?

    Cotard:
    Pierwszy poziom.
    Kwiecista Nicość.

    Powietrze robi się słodkie.
    Zbyt słodkie.
    Duszące.
    W oddali zaczynają się wyłaniać pierwsze kwiaty.
    Delikatne.
    Białe.
    Ich płatki poruszają się mimo, że nie ma wiatru

    Z zachwytem
    Alysia:
    Och…
    Cotard!
    spójrz tylko
    Jak tu pięknie!

    Na jej twarzy pojawia się prawdziwy, ciepły uśmiech.
    Pierwszy od wejścia.


    Cotard:
    Nie podchodź!

    #Alysia:
    #1>Dlaczego?
    #Są niebezpieczne?
    #2>Chcesz powiedzieć, że to…?

    #1>Cotard patrzy na kwiaty.
    #2> Dotyka jednego z kwiatów.

    Jeden z płatków drży
    Potem cofa się.
    Jakby czas na moment się załamał.



    #Cotard:
    #1>Nie.
    #Gorzej.
    #Chcą, abyś została.
    #2>Tak samo jak ja. 
    #Też powoli znikam.

    #Alysia:
    #1>Kwiaty?
    #2> Nie mów tak.


    #Cotard:
    #1>Nie.
    #Całe to miejsce.
    #2>Dlaczego?
    #Ty jedyna nie próbujesz mi wmówić, że żyję.

    #Dziennik Alysii Wpis 002

    Kwiaty.
    Nie potrafię opisać ich piękna.
    Są zbyt doskonałe.
    A przez to nienaturalne.

    Cotard twierdzi, że nie są prawdziwe.
    I co najgorsze…

    wierzę mu.

    Mam jednak dziwne wrażenie, że to miejsce reaguje na emocje.
    Na zachwyt.
    Na lęk.
    Na wspomnienia.

    Im bardziej chcę coś zrozumieć, tym bardziej rzeczywistość wydaje się miękka.
    Jakby można ją było rozerwać palcami.

    Kwiaty drżą.
    Pył unosi się w powietrzu jak złoty dym.
    Z głębi łąki dobiega dźwięk.
    Coś bardziej pomiędzy śmiechem a buczeniem
    PRRRRRRRRRRR.

    Coś małego przelatuje tuż przed twarzą Alysii.
    Odruchowo cofa się o krok.
    Przed nimi zawisa drobna istota.

    Pszczółka:
    Prrr–prrrr!
    OoooOOOO, goście!
    Żywi goście!

    Przekrzywia głowę.
    Patrzy na Cotarda.

    …

    Hhahahahahahahahha
    A nie.
    nie wszyscy
    PRRRR.

    Zaczyna latać wokół niego.

    Ty śmierdzisz!
    Fuj FUJ FUUUJJJ
    Jak stare liście.
    Jak mokry grób.
    Jak coś, co już dawno powinno zostać na dole.
    Prawda Cotard?

    Cotard patrzy na nią pustym wzrokiem.

    Cotard:
    Odejdź.

    Pszczółka:
    Oooodejdź.
    Ooooo odeeejdźź
    Prrrrrrr.

    Alysia mimowolnie się uśmiecha.
    Trochę nerwowo
    Trochę rozbawiona

    Alysia:
    Jesteś… mieszkanką tego miejsca?

    Pszczółka:
    A ty jesteś śmieszna.
    Prrr.
    Pytasz tak, jakby to miejsce miało mieszkańców.
    To miejsce ma tylko to, co zostało
    I to jest SUUUUUUUUUUUUPER


    Alysia:
    A co to znaczy… “ to, co zostało”?

    Pszczółka:
    To, czego Nicość nie połknęła.
    Jeszcze.
    Wspomnienia… żale
    Resztki ludzi.

    Pszczółka znów patrzy na Cotarda

    Albo resztki życia.
    Prrrrrrrrrrrr

    Alysia:
    Przepraszam, że spytam ale…
    Widziałaś może naszych rodziców?
    Badaczy.
    Byli tu lata temu

    Pszczółka:
    OoooooOOOo.
    Tych.
    Prrrrr.
    Tak.
    Widziałam.

    Alysia:
    Co?! Naprawdę?!
    Gdzie?!
    Co się z nimi stało?!

    Pszczółka wykonuje kilka chaotycznych obrotów w powietrzu.
    Pszczółka:
    Pachniesz jak oni.
    Zeszli niżej.
    Niżej.
    Niżej.
    Zawsze niżej.
    Szukali.
    tak jak ty.

    …
    Aleeee
    PRRRR
    Źródło patrzy też w górę.

    Cotard patrzy na nią chłodno.
    Cotard:
    Wiesz coś więcej o rodzicach?.

    Pszczółka śmieje się.
    Pszczółka:
    Prr.
    Czyli jednak ci zależy.
    …
    Przeszli przez łąkę.
    Kłócili się.
    O to, które z nich zaczęło znikać pierwsze.

    Cotard spogląda na Alyssie.
    W jego oczach po raz pierwszy pojawia się cień napięcia.

    Cotard:
    Kiedy?

    Pszczółka:
    Tutaj?
    Tu czas nie istnieje.
    Prr.
    Ale dla Was?
    DAWNO.

    Miło się gadało, lecę zapylać kwiatkiiiii!!!!
    Prrrrrrrrr!

    Pszczółka odlatuje i znika w oddali.

    Alysia i Cotard stoją dłuższą chwilę w ciszy.
    …
    Patrzą na siebie
    Alysia przerywa ciszę
    Zaciska notes przy piersi.

    Alysia:
    Więc…
    Naprawdę tu byli

    Cotard patrzy na nią.

    Cotard:
    Albo to miejsce chce, żebyś w to uwierzyła.

    Alysia:
    A jeśli choć raz nie masz racji?

    Cotard:
    …

    Nagle znów słychać bzyczenie

    Pszczółka:
    Prrrrr!
    Jeśli chcecie znaleźć odpowiedzi…
    schodźcie niżej.
    Ale uważajcie.
    Na następnym poziomie Nicość nie pokazuje już kwiatów.
    Pokazuje prawdę.
    Czyli to, czego najbardziej się boicie.

    Nie zdążyli zareagować.
    Odleciała.



    #IDĄ W DÓŁ

    Z głębi łąki dobiega śmiech.

    Dziecięcy.

    Znajomy.

    Alysia zamiera.

    Uczeń:
    Pani Alysio!

    Na końcu ścieżki stoją dzieci.
    Jej uczniowie.

    Uczeń:
    Wróci Pani?
    Brakuje nam Pani…

    Cotard gwałtownie łapie ją za nadgarstek
    Jego dłoń jest lodowata.

    Cotard:
    Nie patrz na nich!

    Alysia:
    To moi uczniowie!
    Musieli się o mnie martwić!

    Alysia próbuje się wyrwać.
    Cotard zaciska dłoń mocniej.

    Puść mnie Cotard!!!

    Pierwszy raz w jego głosie słychać… GNIEW.

    Cotard:
    NIE.
    to nie oni
    NICOŚĆ wie, czego najbardziej ci brakuje.
    I użyje tego przeciwko tobie.

    Głos.
    Rozbrzmiewa wszędzie.

    NICOŚĆ:
    Jedno.
    Musi.
    Zniknąć.

    Alysia patrzy na Cotarda.
    Alysia:
    Słyszysz to?

    Cotard:
    Tak.
    …
    To nie głos.
    To brak czegoś, co powinno istnieć.

    Wszystko cichnie.
    Nawet kwiaty przestają drżeć.

    Przed nimi ziemia pęka na dwie ścieżki
    Lewa - skąpana w jasnym miękkim świetle
    Prawa - ciemna, pozbawiona koloru.

    Nicość:
    Lewo - Zostań. 

    Prawo - Zejdź niżej. Ale stracisz.

    Alysio.
    Decyzja zależy od Ciebie.

    Zapada cisza.
    Alysia patrzy na swoje dłonie.
    Drżą.

    Cotard:
    Alysio, musisz odpocząć.

    Alysia:
    Ja…
    Nie wiem, co mam zrobić,
    Nie wiem, czy to w ogóle jest wybór.
    Ale czuję, że nie ma tu dobrej decyzji.
    Nie chcę ich stracić…

    Cotard patrzy na iluzje uczniów.
    Na twarzy Alysii maluje się ból.

    Alysia:
    Nie mogę.
    Nie mogę ich tak po prostu usunąć!


    Cotard:
    To nie oni!

    Alysia:
    Skąd wiesz?!!!

    Cotard:
    Bo Nicość nie daje.
    Ona tylko odbiera.
    Nie tworzy życia.

    Alysia:
    A jeśli odbierze mi ich wspomnienia?!

    Cotard:
    Już zaczęła.
    Pamiętasz ich twarze?!
    Pamiętasz jak wyglądała góra?!

    Alysia milknie.
    Oczy jej drżą.
    Próbuje sobie przypomnieć.
    I nie potrafi.
    To ją łamie.

    Alysia:
    …
    nie.

    Cotard:
    No właśnie.

    Alysia:
    Mówisz, że Oni nie istnieją…
    To dlaczego o sobie mówisz to samo?

    Cotard:
    Jeśli tego nie usuniesz…
    Nigdy stąd nie wyjdziesz.

    #WYBÓR GRACZA
    #1> ZOSTAŃ
    #2> IDŹ DALEJ

    #1>
    #Alysia patrzy na swoich uczniów.
    #Ich głosy są miękkie.
    #Znajome.
    #Pełne ciepła
    #Dotyka świetlistej chmury.
    #W tej samej chwili świat mięknie.
    #Kwiaty rozkwitają gwałtownie.
    #Światło zalewa ekran
    #Jej twarz rozluźnia się.
    #Uśmiecha
#
    #Uczeń:
    #Gdzie pani była?
    #Martwiliśmy się.
#
    #Alysia:
    #Ja…
    #chyba się zgubiłam.
    #Ale już wszystko dobrze.
    #Możemy wracać.
#
    #Powoli siada na łące.
    #Kładzie się między kwiatami.
    #Oczy same się zamykają.
#
    #Cotard rzuca się do Alysii
    #Po raz pierwszy jego głos
    #drży.
#
    #Cotard:
    #Alysia…
    #Nie…
    #Proszę…
    #Po jego policzku spływa łza.
#
    #Nie zostawiaj mnie tutaj samego
    #…
    #Nie znikaj.
#
    #Alysia nie odpowiada.
    #Zostaje na łące.
    #Uśpiona przez Nicość.
#
    #Cotard zaczyna płakać.

    ##2> 
    #Alysia zamyka oczy.
    #Łzy zbierają się pod powiekami.
#
    #Alysia:
    #To nie oni.
#
    #Iluzja zaczyna pękać.
    #Światło przygasa.
    #Sylwetki uczniów powoli znikają
#
    #Uczeń:
    #Pani Alysio… dlaczego…?
#
    #Alysia odwraca wzrok
    #Nie potrafi patrzeć.
#
    #Alysia:
    #Przepraszam…
#
    #Uczniowie znikają.
    #Zaczyna płakać
#
    #Świat wokół nich traci kolory.
    #Kwiaty stają się niemal szare.

    Cotard:
    Dobrze
    …
    To jest prawdziwe.

    Alysia:
    Co?

    Cotard:
    To, że ich nie ma
    Wolałem się upewnić.
    … Chodź.
    Idziemy niżej
    Alysia ociera łzy.


    Alysia:
    Zaczynam rozumieć, dlaczego ludzie nie chcą wiedzieć.
    Jeśli każde zejście wymaga poświęcenia to…
    ile z naszych wspomnień zostanie na końcu?
    A jeśli na samym końcu nie zostanie nic?
    to kim będę.



    #KONIEC AKTU 1



    # This ends the game.

    return
