/**
 * PAY O' MAY - OFFICIAL LANDING PAGE SCRIPT
 * Interactive controls for showcase tabs, mobile nav, 50/30/20 budget calculator,
 * and comprehensive bilingual language switching (Indonesian / English).
 */

document.addEventListener('DOMContentLoaded', () => {
    // ------------------------------------------------------------
    // 1. LANGUAGE TRANSLATIONS DICTIONARY
    // ------------------------------------------------------------
    const translations = {
        id: {
            page_title: "Pay o' May - Gim Visual Novel Edukasi Finansial Mahasiswa",
            nav_about: "Tentang",
            nav_features: "Dilema Finansial",
            nav_characters: "Karakter",
            nav_simulator: "Simulasi 50/30/20",
            nav_ending: "Ending",
            nav_download: "Unduh Gim",

            hero_badge: "Visual Novel Edukasi Finansial • Versi 0.3.7",
            hero_title: "Kelola Uang Sakumu,<br><span class=\"gradient-text\">Tentukan Masa Depanmu.</span>",
            hero_desc: "Kamu berperan sebagai seorang mahasiswa yang merantau dengan uang saku bulanan terbatas <strong>Rp 2.000.000</strong>. Mampukah kamu bertahan selama Sebulan di tengah godaan nongkrong FOMO, promo PayLater berbunga, dan keadaan darurat tak terduga?",
            hero_btn_download: "Unduh Sekarang",
            hero_btn_sim: "Simulasi Anggaran 50/30/20",
            hero_btn_gh: "Lihat di GitHub",

            pill_engine: "Engine Ren'Py 8.5",
            pill_platforms: "Windows & Android",
            pill_endings: "4 Variasi Ending",
            pill_simulation: "Simulasi Finansial Nyata",

            mockup_window_title: "Pay o' May - Preview Visual Novel",
            tab_room: "Kamar Kos",
            tab_campus: "Kampus & FOMO",
            tab_report: "Rapor Finansial",
            hud_active_balance: "Saldo Aktif",
            hud_emergency_fund: "Dana Darurat",
            hud_paylater_label: "PayLater",
            hud_paylater: "Rp 0 (Bebas Utang)",
            mockup_tip_title: "Tips Finansial",

            about_tag: "Latar Belakang Cerita",
            about_title: "Kenapa Pay o' May Diciptakan?",
            about_sub: "Transisi dari masa sekolah ke kehidupan mandiri di perantauan adalah fase krusial bagi mahasiswa. Tanpa literasi keuangan yang tepat, kebebasan finansial sering kali berujung pada krisis tanggal tua.",

            card1_title: "Ilusi Uang Saku Awal Bulan",
            card1_desc: "Menerima uang saku utuh di awal bulan membuat mahasiswa merasa kaya raya, sehingga belanja konsumtif dilakukan tanpa memperhitungkan kebutuhan 30 hari ke depan.",

            card2_title: "Jebakan Kemudahan PayLater",
            card2_desc: "Fitur beli sekarang bayar nanti terasa seperti uang gratis, padahal bunga mingguan dan denda keterlambatan mengintai saat uang kiriman bulan depan masuk.",

            card3_title: "Tekanan Sosial & Budaya FOMO",
            card3_desc: "Takut ketinggalan tren kawan sebaya (nongkrong kafe, sewa vila, langganan hiburan) sering memaksa mahasiswa memaksakan gaya hidup di luar batas dompetnya.",

            features_tag: "Mekanika Permainan",
            features_title: "4 Pilar Pembelajaran Finansial",
            features_sub: "Setiap keputusan yang kamu ambil memiliki konsekuensi nyata pada saldo uang jajan, cadangan tabungan, tagihan utang, dan hubungan pertemananmu.",

            feat1_title: "Pay Yourself First (Dana Darurat)",
            feat1_desc: "Belajar mendisiplinkan diri menyisihkan simpanan aman sebelum memakai uang untuk hal lain. Ketika musibah seperti charger laptop rusak terjadi, kamu siap 100% mandiri tanpa merepotkan orang tua.",
            feat1_tag: "Kemandirian Finansial",

            feat2_title: "Formula Anggaran 50 / 30 / 20",
            feat2_desc: "Mempraktikkan pembagian pos ala mahasiswa bersama Michelle: 50% untuk kebutuhan pokok (makan, kos, kuota), 30% untuk hiburan/keinginan, dan 20% untuk tabungan masa depan.",
            feat2_tag: "Prinsip Alokasi Sehat",

            feat3_title: "Simulasi Utang & Bunga PayLater",
            feat3_desc: "Mengalami langsung bagaimana defisit uang jajan otomatis dialihkan ke tagihan PayLater dengan bunga majemuk 5% per minggu yang menggerogoti stabilitas finansialmu.",
            feat3_tag: "Literasi Bahaya Utang",

            feat4_title: "Menegakkan Batasan Finansial Pertemanan",
            feat4_desc: "Mengasah ketegasan emosional untuk menolak ajakan boros atau membatasi nominal saat kawan meminjam uang tanpa merusak kehangatan hubungan pertemanan.",
            feat4_tag: "Financial Boundary",

            tokoh_tag: "Dramatis Personal",
            tokoh_title: "Karakter & Dinamika Cerita",
            tokoh_sub: "Kenali tokoh-tokoh yang akan memengaruhi setiap langkah finansialmu sepanjang 4 minggu di kota perantauan.",

            role_player: "Tokoh Utama",
            char_player_name: "Player (Billa)",
            char_player_sub: "Mahasiswa/i Perantau",
            char_player_quote: "\"Dua juta rupiah untuk sebulan. Rasanya banyak sekali... tapi benarkah begitu?\"",
            char_player_bio: "Seorang mahasiswa/i yang memegang kendali penuh atas uang sakunya. Keputusannya menentukan apakah ia lulus dengan predikat Bendahara Handal atau krisis mie instan.",

            role_fomo: "Representasi FOMO",
            char_axel_name: "Axel",
            char_axel_sub: "Sahabat Impulsif",
            char_axel_quote: "\"Momen ini cuma sekali sebelum UAS! Kalau nggak ikut nongkrong, nyesel loh!\"",
            char_axel_bio: "Teman karib yang gemar nongkrong dan berbelanja spontan. Sumber utama godaan pengeluaran sosial yang menguji pertahanan finansial pemain.",

            role_wise: "Literasi Finansial",
            char_michelle_name: "Michelle",
            char_michelle_sub: "Sahabat Cermat",
            char_michelle_quote: "\"Sejak aku mencatat semua pengeluaran, aku jadi tahu uangku bocor ke mana.\"",
            char_michelle_bio: "Mahasiswi disiplin yang memperkenalkan metode pencatatan kas harian dan alokasi 50/30/20. Menjadi mentor sekaligus tempat bertukar solusi hemat.",

            role_support: "Dukungan Moral",
            char_mama_name: "Mama",
            char_mama_sub: "Orang Tua di Rumah",
            char_mama_quote: "\"Mama percaya kamu bisa atur uang saku sendiri. Jangan sampai kehabisan di tanggal tua ya.\"",
            char_mama_bio: "Pengirim uang saku bulanan yang selalu menaruh kepercayaan besar pada kemampuan mandiri anaknya. Reaksinya di akhir bulan mencerminkan hasil usahamu.",

            sim_tag: "Mini-Widget Interaktif",
            sim_title: "Kalkulator Pos Keuangan 50 / 30 / 20",
            sim_sub: "Geser slider di bawah ini untuk melihat bagaimana rumus emas Michelle membagi uang saku bulananmu secara seimbang!",
            sim_label_allowance: "Nominal Uang Saku Bulanan:",
            sim_mark_1: "Rp 1 Juta",
            sim_mark_2: "Rp 2 Juta (Game)",
            sim_mark_3: "Rp 3 Juta",
            sim_mark_5: "Rp 5 Juta",

            sim_cat_needs: "Kebutuhan Pokok (Needs)",
            sim_desc_needs: "Makan sehari-hari, sewa kos, kuota internet kuliah, perlengkapan mandi, dan transportasi.",
            sim_cat_wants: "Gaya Hidup & Keinginan (Wants)",
            sim_desc_wants: "Nongkrong bareng teman, jajan kopi, langganan serial streaming, dan belanja hobi seperlunya.",
            sim_cat_savings: "Tabungan & Dana Darurat",
            sim_desc_savings: "Tabungan wajib di awal bulan untuk antisipasi darurat medis, servis laptop, atau investasi masa depan.",

            ending_tag: "Hasil Akhir",
            ending_title: "4 Cabang Ending & Gelar Finansial",
            ending_sub: "Skor kesadaran finansial (skala tetap 22 poin) menentukan nasib akhir petualanganmu di penghujung bulan.",

            end_badge_a: "Ending A",
            end_a_title: "Bendahara Handal",
            end_a_cond: "Skor Tinggi • Bebas Utang",
            end_a_desc: "Berhasil mengendalikan seluruh pos anggaran, memiliki sisa uang jajan, dana darurat utuh, dan mampu mentraktir kawan tanpa cemas.",
            end_a_star: "⭐⭐⭐⭐ (Gelar: Financial Master)",

            end_badge_b: "Ending B",
            end_b_title: "Bertahan Aman",
            end_b_cond: "Skor Sedang • Mandiri",
            end_b_desc: "Mampu melewati 31 hari tanpa utang PayLater meskipun saldo tipis dan dana darurat sempat terpakai untuk keperluan mendesak.",
            end_b_star: "⭐⭐⭐ (Gelar: Survivor Rantau)",

            end_badge_c: "Ending C",
            end_c_title: "Jeratan PayLater",
            end_c_cond: "Tagihan Utang Berjalan",
            end_c_desc: "Tergiur kemudahan cicilan konsumtif. Bunga mingguan 5% menumpuk dan uang kiriman bulan berikutnya terancam langsung tersedot.",
            end_c_star: "⭐⭐ (Pelajaran Bunga Berbunga)",

            end_badge_d: "Ending D",
            end_d_title: "Mie Instan Akhir Bulan",
            end_d_cond: "Saldo Habis / Minus",
            end_d_desc: "Belanja impulsif tanpa pos darurat membuat saldo terkuras habis sebelum tanggal 25. Bertahan hidup dengan mie instan dan bantuan darurat.",
            end_d_star: "⭐ (Perlu Remedial Finansial)",

            dl_tag: "Akses Permainan",
            dl_title: "Unduh Gim Pay o' May",
            dl_sub: "Pay o' May tersedia secara gratis untuk perangkat Windows PC dan Android. Pilih platform perangkatmu dan mulailah petualangan mengelola keuangan mandiri!",

            dl_win_title: "Windows PC",
            dl_win_badge: "Standalone Desktop (.zip)",
            dl_win_desc: "Untuk laptop dan PC (Windows 7/8/10/11 64-bit). Cukup unduh, ekstrak berkas zip, dan langsung mainkan via <code>PayoMay.exe</code> tanpa perlu instalasi rumit.",
            dl_win_f1: "Resolusi Full HD 1080p Tajam & Audio BGM Stereo",
            dl_win_f2: "Kontrol Keyboard, Mouse & Pintasan Lengkap",
            dl_win_f3: "Berkas Portabel (Simpan save data lokal)",
            dl_win_btn: "Unduh Versi Windows (.zip)",
            dl_win_sub: "Tautan Unduhan Google Drive",

            dl_and_title: "Android",
            dl_and_badge: "Paket Instalasi (.apk)",
            dl_and_desc: "Untuk smartphone dan tablet (Android 6.0 Marshmallow ke atas). Unduh berkas APK, pasang di ponselmu, dan nikmati petualangan finansial di mana saja.",
            dl_and_f1: "Navigasi Layar Sentuh Responsif & Intuitif",
            dl_and_f2: "100% Offline Tanpa Butuh Kuota Internet",
            dl_and_f3: "Ringan, Performa Halus & Hemat Daya",
            dl_and_btn: "Unduh Versi Android (.apk)",

            dl_note_free: "100% Gratis & Bebas Iklan",
            dl_note_offline: "Offline Playable Tanpa Koneksi Internet",
            dl_note_safe: "Aman & Tanpa Perlu Akun / Registrasi",

            footer_desc: "Gim Visual Novel Interaktif Edukasi Finansial untuk Mahasiswa dan Gen-Z. Rasakan serunya mengatur anggaran mandiri dan hadapi berbagai godaan finansial di dunia perantauan.",
            footer_quick_links: "Navigasi Cepat",
            footer_nav_about: "Latar Belakang",
            footer_nav_dilemmas: "Dilema Finansial",
            footer_nav_characters: "Karakter",
            footer_nav_calculator: "Kalkulator 50/30/20",
            footer_nav_download: "Unduh Gim",

            footer_credit_heading: "Kredit & Lisensi Aset",
            footer_credit_text: "<strong>Karya Gim Indie:</strong> Dikembangkan oleh Hyenavia.<br><strong>Engine:</strong> Ren'Py Visual Novel Engine.<br><br><strong>Lisensi Aset:</strong> Creative Commons BY 4.0 (Kevin MacLeod) & Everyday Life UI by DadddyDarko.",
            footer_copyright: "&copy; 2026 Pay o' May. Semua hak cipta dilindungi."
        },
        en: {
            page_title: "Pay o' May - Educational Student Financial Awareness Visual Novel",
            nav_about: "About",
            nav_features: "Financial Dilemmas",
            nav_characters: "Characters",
            nav_simulator: "50/30/20 Simulation",
            nav_ending: "Endings",
            nav_download: "Download Game",

            hero_badge: "Financial Education Visual Novel • Version 0.3.7",
            hero_title: "Manage Your Allowance,<br><span class=\"gradient-text\">Shape Your Future.</span>",
            hero_desc: "Play as a college student living away from home with a monthly allowance of <strong>Rp 2,000,000</strong>. Can you survive a full month amidst FOMO peer pressure, enticing PayLater loans, and unforeseen emergencies?",
            hero_btn_download: "Download Now",
            hero_btn_sim: "50/30/20 Budget Calculator",
            hero_btn_gh: "View on GitHub",

            pill_engine: "Ren'Py 8.5 Engine",
            pill_platforms: "Windows & Android",
            pill_endings: "4 Unique Endings",
            pill_simulation: "Realistic Financial Simulation",

            mockup_window_title: "Pay o' May - Visual Novel Preview",
            tab_room: "Dorm Room",
            tab_campus: "Campus & FOMO",
            tab_report: "Financial Report",
            hud_active_balance: "Active Balance",
            hud_emergency_fund: "Emergency Fund",
            hud_paylater_label: "PayLater",
            hud_paylater: "Rp 0 (Debt Free)",
            mockup_tip_title: "Financial Tip",

            about_tag: "Background Story",
            about_title: "Why Was Pay o' May Created?",
            about_sub: "Transitioning from high school to living independently is a crucial milestone for university students. Without proper financial literacy, personal freedom often leads to an end-of-the-month financial crisis.",

            card1_title: "Early-Month Allowance Illusion",
            card1_desc: "Receiving an entire allowance upfront creates a false sense of wealth, encouraging impulse shopping without considering essentials for the remaining 30 days.",

            card2_title: "The Convenient PayLater Trap",
            card2_desc: "Buy-now-pay-later services feel like free money, but weekly interest and late penalties quietly consume next month's allowance before it even arrives.",

            card3_title: "Social Pressure & FOMO Culture",
            card3_desc: "The fear of missing out on peer activities (cafe hangouts, weekend trips, premium subscriptions) tempts students into living beyond their financial means.",

            features_tag: "Core Mechanics",
            features_title: "4 Pillars of Financial Learning",
            features_sub: "Every decision you make carries real consequences on your living allowance, emergency savings, debt bills, and friendships.",

            feat1_title: "Pay Yourself First (Emergency Fund)",
            feat1_desc: "Build the discipline to set aside safe savings before spending money on anything else. When emergencies strike like a broken laptop charger, you are 100% self-reliant without troubling your parents.",
            feat1_tag: "Financial Independence",

            feat2_title: "50 / 30 / 20 Budgeting Formula",
            feat2_desc: "Practice student-friendly budgeting with Michelle: 50% for core needs (meals, dorm rent, study data), 30% for entertainment/wants, and 20% for future savings.",
            feat2_tag: "Healthy Allocation Rule",

            feat3_title: "PayLater Debt & Compounding Interest",
            feat3_desc: "Experience firsthand how allowance deficits automatically roll over into PayLater debt with 5% weekly compounding interest eating away at your financial stability.",
            feat3_tag: "Debt Hazard Literacy",

            feat4_title: "Upholding Social Financial Boundaries",
            feat4_desc: "Sharpen emotional firmness to decline lavish peer invites or cap loan amounts when friends ask to borrow money without hurting friendships.",
            feat4_tag: "Financial Boundary",

            tokoh_tag: "Personal Dynamics",
            tokoh_title: "Characters & Story Dynamics",
            tokoh_sub: "Meet the cast of characters who will influence every financial choice you make across 4 weeks in college.",

            role_player: "Main Character",
            char_player_name: "Player (Billa)",
            char_player_sub: "College Student",
            char_player_quote: "\"Two million rupiah for a month. It feels like a lot... but is it really?\"",
            char_player_bio: "A college student with full control over their allowance. Their decisions dictate whether they finish the month as a Master Treasurer or face an instant noodle crisis.",

            role_fomo: "FOMO Representative",
            char_axel_name: "Axel",
            char_axel_sub: "Impulsive Best Friend",
            char_axel_quote: "\"This moment only happens once before finals! If you skip hanging out, you'll regret it!\"",
            char_axel_bio: "A close friend who loves hanging out and impulse buying. The primary source of social FOMO temptations that test the player's financial discipline.",

            role_wise: "Financial Literacy",
            char_michelle_name: "Michelle",
            char_michelle_sub: "Prudent Best Friend",
            char_michelle_quote: "\"Ever since I tracked every expense, I know exactly where my money was leaking.\"",
            char_michelle_bio: "A disciplined student who introduces daily cash logging and the 50/30/20 allocation. Your mentor and reliable guide for frugal solutions.",

            role_support: "Moral Support",
            char_mama_name: "Mom",
            char_mama_sub: "Parent Back Home",
            char_mama_quote: "\"Mom trusts you to manage your own allowance. Just don't run completely empty before the month ends.\"",
            char_mama_bio: "The sender of your monthly allowance who puts immense trust in your independence. Her end-of-month reaction reflects your financial stewardship.",

            sim_tag: "Interactive Mini-Widget",
            sim_title: "50 / 30 / 20 Budget Calculator",
            sim_sub: "Slide the amount below to see how Michelle's golden formula balances your monthly allowance!",
            sim_label_allowance: "Monthly Allowance Amount:",
            sim_mark_1: "Rp 1 Million",
            sim_mark_2: "Rp 2 Million (Game)",
            sim_mark_3: "Rp 3 Million",
            sim_mark_5: "Rp 5 Million",

            sim_cat_needs: "Essential Needs (Needs)",
            sim_desc_needs: "Daily meals, dorm rent, study internet data, toiletries, and local transportation.",
            sim_cat_wants: "Lifestyle & Leisure (Wants)",
            sim_desc_wants: "Hanging out with friends, artisan coffee, streaming subscriptions, and hobby splurges.",
            sim_cat_savings: "Savings & Emergency Fund",
            sim_desc_savings: "Essential savings set aside on day one for medical emergencies, laptop repairs, or future investments.",

            ending_tag: "Story Endings",
            ending_title: "4 Story Endings & Financial Titles",
            ending_sub: "Your financial awareness score (fixed 22-point scale) determines the final outcome at the end of the month.",

            end_badge_a: "Ending A",
            end_a_title: "Master Treasurer",
            end_a_cond: "High Score • Debt Free",
            end_a_desc: "Successfully controlled all budget categories, kept emergency savings intact, and enjoyed treating friends without financial anxiety.",
            end_a_star: "⭐⭐⭐⭐ (Title: Financial Master)",

            end_badge_b: "Ending B",
            end_b_title: "Safe Survivor",
            end_b_cond: "Moderate Score • Independent",
            end_b_desc: "Survived 31 days free of PayLater debt, even though the final balance was tight and emergency savings had to be tapped.",
            end_b_star: "⭐⭐⭐ (Title: Resilient Survivor)",

            end_badge_c: "Ending C",
            end_c_title: "PayLater Trap",
            end_c_cond: "Active Outstanding Debt",
            end_c_desc: "Seduced by frictionless consumer installments. Weekly 5% interest compounded, and next month's allowance is already pledged to debts.",
            end_c_star: "⭐⭐ (Compounding Interest Lesson)",

            end_badge_d: "Ending D",
            end_d_title: "Instant Noodle Crisis",
            end_d_cond: "Zero or Negative Balance",
            end_d_desc: "Impulsive spending without an emergency buffer depleted funds before the 25th. Left surviving on instant noodles and emergency bailouts.",
            end_d_star: "⭐ (Needs Financial Remedial)",

            dl_tag: "Game Access",
            dl_title: "Download Pay o' May",
            dl_sub: "Pay o' May is available for free on Windows PC and Android. Choose your platform and begin your financial independence journey!",

            dl_win_title: "Windows PC",
            dl_win_badge: "Standalone Desktop (.zip)",
            dl_win_desc: "For laptops and desktops (Windows 7/8/10/11 64-bit). Download, extract the zip file, and play instantly via <code>PayoMay.exe</code> without complex installation.",
            dl_win_f1: "Crisp Full HD 1080p Visuals & Stereo BGM Audio",
            dl_win_f2: "Full Keyboard, Mouse & Shortcut Navigation",
            dl_win_f3: "Portable Files (Local save data management)",
            dl_win_btn: "Download Windows Version (.zip)",
            dl_win_sub: "Google Drive Download Link",

            dl_and_title: "Android",
            dl_and_badge: "Installable Package (.apk)",
            dl_and_desc: "For smartphones and tablets (Android 6.0 Marshmallow or higher). Download the APK file, install on your device, and enjoy financial gaming anywhere.",
            dl_and_f1: "Responsive & Intuitive Touchscreen Controls",
            dl_and_f2: "100% Offline Without Needing Mobile Data",
            dl_and_f3: "Lightweight, Smooth Performance & Battery Efficient",
            dl_and_btn: "Download Android Version (.apk)",

            dl_note_free: "100% Free & Ad-Free",
            dl_note_offline: "Fully Playable Offline",
            dl_note_safe: "Safe & No Registration Required",

            footer_desc: "An interactive financial literacy visual novel for college students and Gen-Z. Experience the challenge of budgeting independently while navigating financial temptations.",
            footer_quick_links: "Quick Navigation",
            footer_nav_about: "Background",
            footer_nav_dilemmas: "Financial Dilemmas",
            footer_nav_characters: "Characters",
            footer_nav_calculator: "50/30/20 Calculator",
            footer_nav_download: "Download Game",

            footer_credit_heading: "Credits & Asset Licenses",
            footer_credit_text: "<strong>Indie Game Project:</strong> Developed by Hyenavia.<br><strong>Engine:</strong> Ren'Py Visual Novel Engine.<br><br><strong>Asset Licenses:</strong> Creative Commons BY 4.0 (Kevin MacLeod) & Everyday Life UI by DadddyDarko.",
            footer_copyright: "&copy; 2026 Pay o' May. All rights reserved."
        }
    };

    let currentLang = localStorage.getItem('payomay_lang') || 'id';

    function setLanguage(lang) {
        if (!translations[lang]) return;
        currentLang = lang;
        localStorage.setItem('payomay_lang', lang);

        document.documentElement.lang = lang;

        // Update document tab title
        if (translations[lang] && translations[lang].page_title) {
            document.title = translations[lang].page_title;
        }

        // Update active class on buttons
        const langBtns = document.querySelectorAll('.lang-btn');
        langBtns.forEach(btn => {
            if (btn.getAttribute('data-lang') === lang) {
                btn.classList.add('active');
            } else {
                btn.classList.remove('active');
            }
        });

        // Translate all data-i18n elements
        const elements = document.querySelectorAll('[data-i18n]');
        elements.forEach(el => {
            const key = el.getAttribute('data-i18n');
            if (translations[lang] && translations[lang][key] !== undefined) {
                el.innerHTML = translations[lang][key];
            }
        });

        // Update active scene quote
        const activeTab = document.querySelector('.showcase-tab.active');
        if (activeTab) {
            const targetImg = activeTab.getAttribute('data-img');
            if (targetImg && showcaseQuote && sceneQuotes[currentLang] && sceneQuotes[currentLang][targetImg]) {
                showcaseQuote.textContent = sceneQuotes[currentLang][targetImg];
            }
        }

        // Re-run budget calculation to refresh localized advice text
        if (budgetSlider) {
            updateBudgetCalc(parseInt(budgetSlider.value, 10));
        }
    }

    // ------------------------------------------------------------
    // 2. NAVBAR SCROLL & MOBILE TOGGLE
    // ------------------------------------------------------------
    const navbar = document.getElementById('navbar');
    const navToggle = document.getElementById('nav-toggle');
    const navMenu = document.getElementById('nav-menu');
    const navLinks = document.querySelectorAll('.nav-link');

    window.addEventListener('scroll', () => {
        if (window.scrollY > 40) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    if (navToggle && navMenu) {
        navToggle.addEventListener('click', () => {
            navMenu.classList.toggle('active');
            navToggle.classList.toggle('open');
        });

        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                navMenu.classList.remove('active');
                navToggle.classList.remove('open');
            });
        });
    }

    // Language switch click handler
    const langBtns = document.querySelectorAll('.lang-btn');
    langBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const lang = btn.getAttribute('data-lang');
            setLanguage(lang);
        });
    });

    // ------------------------------------------------------------
    // 3. HERO SHOWCASE TABS INTERACTION
    // ------------------------------------------------------------
    const showcaseTabs = document.querySelectorAll('.showcase-tab');
    const showcaseImg = document.getElementById('showcase-img');
    const showcaseQuote = document.getElementById('showcase-quote');
    const hudSaldo = document.getElementById('hud-saldo');

    const sceneQuotes = {
        id: {
            'images/bg kos.png': '"Awal bulan. Uang saku Rp 2.000.000 dari Mama sudah masuk. Keputusan pertama ada di tanganmu."',
            'images/bg kampus.png': '"Axel: Bro, ayo nongkrong di kafe viral baru itu! Masa cuma kamu yang nggak ikut?"',
            'images/cover_midnight.png': '"Evaluasi kesadaran finansial: apakah kamu berhasil menjadi Bendahara Handal atau krisis di akhir bulan?"'
        },
        en: {
            'images/bg kos.png': '"Start of the month. The Rp 2,000,000 allowance from Mom has arrived. The first decision is in your hands."',
            'images/bg kampus.png': '"Axel: Bro, let\'s hang out at that new viral cafe! Are you really gonna be the only one missing out?"',
            'images/cover_midnight.png': '"Financial awareness evaluation: will you become a Master Treasurer or face an end-of-month crisis?"'
        }
    };

    const sceneSaldo = {
        'images/bg kos.png': 'Rp 1.700.000',
        'images/bg kampus.png': 'Rp 1.450.000',
        'images/cover_midnight.png': 'Rp 450.000'
    };

    showcaseTabs.forEach(tab => {
        tab.addEventListener('click', () => {
            showcaseTabs.forEach(t => t.classList.remove('active'));
            tab.classList.add('active');

            const targetImg = tab.getAttribute('data-img');
            if (targetImg && showcaseImg) {
                showcaseImg.style.opacity = '0.3';
                setTimeout(() => {
                    showcaseImg.src = targetImg;
                    showcaseImg.style.opacity = '1';
                }, 150);
            }

            if (showcaseQuote && sceneQuotes[currentLang] && sceneQuotes[currentLang][targetImg]) {
                showcaseQuote.textContent = sceneQuotes[currentLang][targetImg];
            }

            if (hudSaldo && sceneSaldo[targetImg]) {
                hudSaldo.textContent = sceneSaldo[targetImg];
            }
        });
    });

    // ------------------------------------------------------------
    // 4. KALKULATOR INTERAKTIF 50 / 30 / 20
    // ------------------------------------------------------------
    const budgetSlider = document.getElementById('budget-slider');
    const budgetDisplay = document.getElementById('budget-display');
    const valNeeds = document.getElementById('val-needs');
    const valWants = document.getElementById('val-wants');
    const valSavings = document.getElementById('val-savings');
    const calcAdvice = document.getElementById('calc-advice');

    function formatRupiah(number) {
        return 'Rp ' + number.toLocaleString('id-ID');
    }

    function updateBudgetCalc(amount) {
        const needs = Math.round(amount * 0.5);
        const wants = Math.round(amount * 0.3);
        const savings = Math.round(amount * 0.2);

        if (budgetDisplay) budgetDisplay.textContent = formatRupiah(amount);
        if (valNeeds) valNeeds.textContent = formatRupiah(needs);
        if (valWants) valWants.textContent = formatRupiah(wants);
        if (valSavings) valSavings.textContent = formatRupiah(savings);

        if (calcAdvice) {
            let adviceHtml = '';
            if (currentLang === 'en') {
                if (amount <= 1500000) {
                    adviceHtml = `<strong>Michelle's Advice:</strong> With an allowance of ${formatRupiah(amount)}, you must strictly limit your leisure spending (${formatRupiah(wants)}). Cooking meals in your dorm is your ultimate lifesaver!`;
                } else if (amount <= 2500000) {
                    adviceHtml = `<strong>Michelle's Advice:</strong> An allowance of ${formatRupiah(amount)} is ideal for the 50/30/20 rule. Setting aside ${formatRupiah(savings)} at the start of the month gives you 100% peace of mind against emergencies!`;
                } else {
                    adviceHtml = `<strong>Michelle's Advice:</strong> Having an allowance of ${formatRupiah(amount)} is a golden opportunity. Your monthly savings of ${formatRupiah(savings)} can be invested into mutual funds or career prep!`;
                }
            } else {
                if (amount <= 1500000) {
                    adviceHtml = `<strong>Nasihat Michelle:</strong> Dengan uang saku ${formatRupiah(amount)}, kamu harus sangat ketat membatasi jajan (${formatRupiah(wants)}). Masak sendiri di kos adalah penyelamat terbaikmu!`;
                } else if (amount <= 2500000) {
                    adviceHtml = `<strong>Nasihat Michelle:</strong> Uang saku ${formatRupiah(amount)} sangat ideal untuk formula 50/30/20. Menyisihkan ${formatRupiah(savings)} di awal bulan melindungimu 100% saat keadaan darurat terjadi!`;
                } else {
                    adviceHtml = `<strong>Nasihat Michelle:</strong> Memiliki uang saku ${formatRupiah(amount)} adalah kesempatan emas. Alokasi tabungan ${formatRupiah(savings)} per bulan bisa mulai diinvestasikan ke reksadana atau modal magang!`;
                }
            }

            calcAdvice.innerHTML = `
                <span class="advice-icon">💡</span>
                <span class="advice-text">${adviceHtml}</span>
            `;
        }
    }

    if (budgetSlider) {
        budgetSlider.addEventListener('input', (e) => {
            const currentVal = parseInt(e.target.value, 10);
            updateBudgetCalc(currentVal);
        });

        // Inisialisasi awal
        updateBudgetCalc(parseInt(budgetSlider.value, 10));
    }

    // Apply stored or default language on page load
    setLanguage(currentLang);
});
