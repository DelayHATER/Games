<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MBTI로 포켓몬 찾기</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/tone/14.8.49/Tone.js"></script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Jua&family=Noto+Sans+KR:wght@400;600;800&display=swap');

    * {
      box-sizing: border-box;
      font-family: 'Jua', 'Noto Sans KR', sans-serif;
    }

    body {
      margin: 0;
      min-height: 100vh;
      background: radial-gradient(circle at 50% 20%, #fffde6 0%, #ffe999 100%);
      color: #5b4428;
      overflow-x: hidden;
    }

    .poke-shadow {
      filter: drop-shadow(0 12px 16px rgba(104, 73, 18, 0.18));
    }

    @keyframes float {
      0%, 100% { transform: translateY(0px) rotate(0deg); }
      50% { transform: translateY(-10px) rotate(2deg); }
    }

    .floating {
      animation: float 3.5s ease-in-out infinite;
    }

    @keyframes pulse-glow {
      0%, 100% { box-shadow: 0 0 15px rgba(255, 215, 0, 0.6); }
      50% { box-shadow: 0 0 30px rgba(255, 165, 0, 0.9); }
    }

    .glow-card {
      animation: pulse-glow 3s infinite;
    }

    /* Custom scrollbar */
    ::-webkit-scrollbar {
      width: 8px;
    }
    ::-webkit-scrollbar-track {
      background: #fff3cc;
    }
    ::-webkit-scrollbar-thumb {
      background: #eac056;
      border-radius: 4px;
    }
  </style>
</head>

<body class="flex flex-col items-center justify-between min-h-screen p-4 sm:p-6">

  <canvas id="bgCanvas" class="fixed inset-0 pointer-events-none z-0"></canvas>

  <button id="fullscreenBtn" class="fixed top-4 right-4 z-50 bg-white/80 hover:bg-white text-amber-900 border-2 border-amber-300 font-bold px-4 py-2 rounded-2xl shadow-lg transition transform hover:scale-105 active:scale-95 text-sm sm:text-base flex items-center gap-2">
    🔲 전체화면
  </button>

  <main class="app w-full max-w-2xl mx-auto z-10 my-auto py-8">

    <header class="header text-center mb-8">
      <div class="ball text-6xl sm:text-7xl mb-2 floating select-none cursor-pointer" id="pokeBallIcon" title="볼을 눌러보세요!">⚡</div>
      <h1 class="text-4xl sm:text-5xl font-extrabold text-amber-900 tracking-tight drop-shadow-sm">MBTI로 포켓몬 찾기</h1>
      <p class="subtitle mt-2 text-amber-700 text-base sm:text-lg">나와 가장 소울메이트인 포켓몬은 누구일까?</p>
    </header>

    <section class="card bg-white/90 backdrop-blur-md border-4 border-amber-300 rounded-3xl p-6 sm:p-10 shadow-2xl relative">

      <!-- MBTI 선택 화면 -->
      <div id="selection" class="transition-all duration-300">
        <div class="question text-center mb-6 text-xl sm:text-2xl font-bold text-amber-800">
          ✨ 나의 MBTI 유형을 골라보세요! ✨
        </div>

        <div class="mbti-grid grid grid-cols-2 sm:grid-cols-4 gap-3 sm:gap-4">
          <!-- 각 MBTI 버튼 -->
          <button class="mbti-btn border-2 border-amber-200 bg-amber-50 hover:bg-amber-100 hover:border-amber-400 text-amber-900 rounded-2xl py-4 text-lg font-extrabold transition transform hover:-translate-y-1 shadow-sm active:scale-95" data-type="ISTJ">ISTJ</button>
          <button class="mbti-btn border-2 border-amber-200 bg-amber-50 hover:bg-amber-100 hover:border-amber-400 text-amber-900 rounded-2xl py-4 text-lg font-extrabold transition transform hover:-translate-y-1 shadow-sm active:scale-95" data-type="ISFJ">ISFJ</button>
          <button class="mbti-btn border-2 border-amber-200 bg-amber-50 hover:bg-amber-100 hover:border-amber-400 text-amber-900 rounded-2xl py-4 text-lg font-extrabold transition transform hover:-translate-y-1 shadow-sm active:scale-95" data-type="INFJ">INFJ</button>
          <button class="mbti-btn border-2 border-amber-200 bg-amber-50 hover:bg-amber-100 hover:border-amber-400 text-amber-900 rounded-2xl py-4 text-lg font-extrabold transition transform hover:-translate-y-1 shadow-sm active:scale-95" data-type="INTJ">INTJ</button>

          <button class="mbti-btn border-2 border-amber-200 bg-amber-50 hover:bg-amber-100 hover:border-amber-400 text-amber-900 rounded-2xl py-4 text-lg font-extrabold transition transform hover:-translate-y-1 shadow-sm active:scale-95" data-type="ISTP">ISTP</button>
          <button class="mbti-btn border-2 border-amber-200 bg-amber-50 hover:bg-amber-100 hover:border-amber-400 text-amber-900 rounded-2xl py-4 text-lg font-extrabold transition transform hover:-translate-y-1 shadow-sm active:scale-95" data-type="ISFP">ISFP</button>
          <button class="mbti-btn border-2 border-amber-200 bg-amber-50 hover:bg-amber-100 hover:border-amber-400 text-amber-900 rounded-2xl py-4 text-lg font-extrabold transition transform hover:-translate-y-1 shadow-sm active:scale-95" data-type="INFP">INFP</button>
          <button class="mbti-btn border-2 border-amber-200 bg-amber-50 hover:bg-amber-100 hover:border-amber-400 text-amber-900 rounded-2xl py-4 text-lg font-extrabold transition transform hover:-translate-y-1 shadow-sm active:scale-95" data-type="INTP">INTP</button>

          <button class="mbti-btn border-2 border-amber-200 bg-amber-50 hover:bg-amber-100 hover:border-amber-400 text-amber-900 rounded-2xl py-4 text-lg font-extrabold transition transform hover:-translate-y-1 shadow-sm active:scale-95" data-type="ESTP">ESTP</button>
          <button class="mbti-btn border-2 border-amber-200 bg-amber-50 hover:bg-amber-100 hover:border-amber-400 text-amber-900 rounded-2xl py-4 text-lg font-extrabold transition transform hover:-translate-y-1 shadow-sm active:scale-95" data-type="ESFP">ESFP</button>
          <button class="mbti-btn border-2 border-amber-200 bg-amber-50 hover:bg-amber-100 hover:border-amber-400 text-amber-900 rounded-2xl py-4 text-lg font-extrabold transition transform hover:-translate-y-1 shadow-sm active:scale-95" data-type="ENFP">ENFP</button>
          <button class="mbti-btn border-2 border-amber-200 bg-amber-50 hover:bg-amber-100 hover:border-amber-400 text-amber-900 rounded-2xl py-4 text-lg font-extrabold transition transform hover:-translate-y-1 shadow-sm active:scale-95" data-type="ENTP">ENTP</button>

          <button class="mbti-btn border-2 border-amber-200 bg-amber-50 hover:bg-amber-100 hover:border-amber-400 text-amber-900 rounded-2xl py-4 text-lg font-extrabold transition transform hover:-translate-y-1 shadow-sm active:scale-95" data-type="ESTJ">ESTJ</button>
          <button class="mbti-btn border-2 border-amber-200 bg-amber-50 hover:bg-amber-100 hover:border-amber-400 text-amber-900 rounded-2xl py-4 text-lg font-extrabold transition transform hover:-translate-y-1 shadow-sm active:scale-95" data-type="ESFJ">ESFJ</button>
          <button class="mbti-btn border-2 border-amber-200 bg-amber-50 hover:bg-amber-100 hover:border-amber-400 text-amber-900 rounded-2xl py-4 text-lg font-extrabold transition transform hover:-translate-y-1 shadow-sm active:scale-95" data-type="ENFJ">ENFJ</button>
          <button class="mbti-btn border-2 border-amber-200 bg-amber-50 hover:bg-amber-100 hover:border-amber-400 text-amber-900 rounded-2xl py-4 text-lg font-extrabold transition transform hover:-translate-y-1 shadow-sm active:scale-95" data-type="ENTJ">ENTJ</button>
        </div>
      </div>

      <!-- 결과 화면 -->
      <div id="result" class="result hidden text-center animate-fade-in">
        <div id="resultMbti" class="inline-block px-4 py-1.5 rounded-full bg-amber-200 text-amber-900 font-extrabold text-sm mb-4 shadow-sm"></div>

        <div id="pokemonEmoji" class="pokemon-emoji text-8xl sm:text-9xl my-4 floating poke-shadow select-none"></div>

        <h2 id="pokemonName" class="pokemon-name text-3xl sm:text-4xl font-extrabold text-amber-900 tracking-tight"></h2>

        <p id="reason" class="reason max-w-lg mx-auto my-4 text-amber-800 text-base sm:text-lg leading-relaxed"></p>

        <div class="compatibility max-w-lg mx-auto my-6 p-4 rounded-2xl bg-amber-50 border-2 border-amber-200 shadow-inner">
          <div class="compatibility-label text-xs sm:text-sm text-amber-700 font-bold mb-1">✨ 최고의 궁합 MBTI</div>
          <div id="compatibilityType" class="compatibility-type text-xl sm:text-2xl font-black text-amber-900"></div>
        </div>

        <div class="flex flex-wrap gap-3 justify-center mt-6">
          <button id="shareBtn" class="bg-amber-500 hover:bg-amber-600 text-white font-extrabold px-6 py-3 rounded-2xl shadow-lg transition transform hover:-translate-y-0.5 active:scale-95 flex items-center gap-2">
            📋 결과 복사하기
          </button>
          <button id="resetBtn" class="bg-amber-700 hover:bg-amber-800 text-white font-extrabold px-6 py-3 rounded-2xl shadow-lg transition transform hover:-translate-y-0.5 active:scale-95">
            ↩ 다시 고르기
          </button>
        </div>
      </div>

    </section>

    <!-- 알림 메시지 박스 -->
    <div id="toast" class="fixed bottom-6 left-1/2 transform -translate-x-1/2 bg-neutral-900 text-white px-6 py-3 rounded-2xl shadow-2xl opacity-0 pointer-events-none transition-all duration-300 z-50 text-sm font-bold">
      클립보드에 복사되었습니다! 🎉
    </div>

    <footer class="footer text-center mt-6 text-amber-800/80 text-sm font-semibold">
      재미로 즐기는 MBTI × 포켓몬 테스트예요! 💖
    </footer>

  </main>

  <script>
    // 포켓몬 데이터베이스
    const pokemonData = {
      ISTJ: {
        name: "메타그로스",
        emoji: "🤖",
        reason: "차분하고 책임감이 강한 ISTJ에게는 냉철하고 체계적인 메타그로스가 잘 어울려요.<br>복잡한 문제도 논리적으로 하나씩 해결하는 모습이 닮았답니다.",
        compatible: "ESFP"
      },
      ISFJ: {
        name: "해피너스",
        emoji: "🥚",
        reason: "다른 사람을 세심하게 챙기는 ISFJ에게 따뜻한 해피너스는 찰떡이에요.<br>든든하게 곁을 지켜주면서 주변에 행복을 나눠주는 모습이 닮았어요.",
        compatible: "ESTP"
      },
      INFJ: {
        name: "가디안",
        emoji: "🧚",
        reason: "깊은 생각과 따뜻한 마음을 가진 INFJ에게 가디안이 잘 어울려요.<br>소중한 사람을 위해 용기를 내는 헌신적인 모습이 INFJ와 닮았답니다.",
        compatible: "ENFP"
      },
      INTJ: {
        name: "뮤츠",
        emoji: "🧬",
        reason: "전략을 세우고 깊이 생각하는 INTJ에게 강력하고 지적인 뮤츠가 어울려요.<br>혼자서도 목표를 향해 꾸준히 나아가는 모습이 멋진 조합이에요.",
        compatible: "ENFP"
      },
      ISTP: {
        name: "루카리오",
        emoji: "🥋",
        reason: "실용적이고 침착한 ISTP에게는 행동으로 보여주는 루카리오가 잘 맞아요.<br>상황을 빠르게 파악하고 필요한 순간 정확하게 움직이는 타입이에요.",
        compatible: "ESFJ"
      },
      ISFP: {
        name: "이브이",
        emoji: "🦊",
        reason: "자유롭고 감각적인 ISFP에게 귀엽고 다채로운 매력의 이브이가 잘 어울려요.<br>정해진 틀보다 자신만의 방식으로 성장하는 모습이 닮았답니다.",
        compatible: "ENFJ"
      },
      INFP: {
        name: "세레비",
        emoji: "🌿",
        reason: "상상력이 풍부하고 마음이 따뜻한 INFP에게 신비로운 세레비가 잘 어울려요.<br>평화와 아름다움을 소중하게 생각하는 모습이 INFP의 감성과 닮았어요.",
        compatible: "ENFJ"
      },
      INTP: {
        name: "프리져",
        emoji: "❄️",
        reason: "호기심 많고 독창적인 INTP에게 신비롭고 차분한 프리져가 어울려요.<br>혼자 생각할 시간을 즐기면서 자신만의 세계를 만들어가는 타입이에요.",
        compatible: "ENTJ"
      },
      ESTP: {
        name: "리자몽",
        emoji: "🔥",
        reason: "대담하고 행동력이 뛰어난 ESTP에게 강렬한 리자몽이 딱이에요.<br>새로운 상황을 두려워하지 않고 직접 부딪히는 에너지가 닮았답니다.",
        compatible: "ISFJ"
      },
      ESFP: {
        name: "피카츄",
        emoji: "⚡",
        reason: "밝고 사람들과 어울리는 것을 좋아하는 ESFP에게 피카츄만큼 잘 맞는 포켓몬은 없죠!<br>주변에 활기를 불어넣고 즐거운 순간을 만드는 매력이 닮았어요.",
        compatible: "ISTJ"
      },
      ENFP: {
        name: "토게피",
        emoji: "🐣",
        reason: "호기심 많고 긍정적인 ENFP에게 사랑스러운 토게피가 잘 어울려요.<br>새로운 가능성을 발견하고 주변 사람에게 좋은 에너지를 전하는 모습이 닮았답니다.",
        compatible: "INFJ"
      },
      ENTP: {
        name: "팬텀",
        emoji: "👻",
        reason: "재치 있고 새로운 아이디어를 좋아하는 ENTP에게 장난꾸러기 팬텀이 어울려요.<br>예상 밖의 행동과 톡톡 튀는 발상으로 분위기를 바꾸는 매력이 닮았어요.",
        compatible: "INFJ"
      },
      ESTJ: {
        name: "거북왕",
        emoji: "🐢",
        reason: "현실적이고 추진력이 강한 ESTJ에게 믿음직한 거북왕이 잘 어울려요.<br>목표를 정하면 꾸준히 밀어붙이고 팀을 든든하게 이끄는 모습이 닮았답니다.",
        compatible: "ISFP"
      },
      ESFJ: {
        name: "푸린",
        emoji: "🎤",
        reason: "사람을 좋아하고 분위기를 따뜻하게 만드는 ESFJ에게 푸린이 잘 어울려요.<br>주변 사람들과 함께 즐거움을 나누고 싶은 마음이 닮았어요.",
        compatible: "ISTP"
      },
      ENFJ: {
        name: "라프라스",
        emoji: "🌊",
        reason: "사람을 이끌면서도 따뜻하게 챙기는 ENFJ에게 라프라스가 잘 어울려요.<br>다른 사람을 도와주고 함께 앞으로 나아가려는 다정한 모습이 닮았답니다.",
        compatible: "INFP"
      },
      ENTJ: {
        name: "망나뇽",
        emoji: "🐉",
        reason: "목표 지향적이고 자신감 있는 ENTJ에게 강력하면서도 믿음직한 망나뇽이 어울려요.<br>큰 목표를 향해 거침없이 나아가면서도 동료를 지켜주는 모습이 멋진 조합이에요.",
        compatible: "INTP"
      }
    };

    // 사운드 이펙트 설정 (Tone.js)
    let synth = null;
    function initSound() {
      if (!synth) {
        synth = new Tone.Synth({
          oscillator: { type: "triangle" },
          envelope: { attack: 0.005, decay: 0.1, sustain: 0.1, release: 0.5 }
        }).toDestination();
      }
    }

    function playPopSound() {
      try {
        initSound();
        Tone.start();
        synth.triggerAttackRelease("C5", "8n");
      } catch (e) {
        // audio context blocked or unsupported
      }
    }

    function playSuccessSound() {
      try {
        initSound();
        Tone.start();
        const now = Tone.now();
        synth.triggerAttackRelease("G4", "8n", now);
        synth.triggerAttackRelease("C5", "8n", now + 0.1);
        synth.triggerAttackRelease("E5", "4n", now + 0.2);
      } catch (e) {}
    }

    // DOM 요소
    const selection = document.getElementById("selection");
    const result = document.getElementById("result");
    const resultMbti = document.getElementById("resultMbti");
    const pokemonEmoji = document.getElementById("pokemonEmoji");
    const pokemonName = document.getElementById("pokemonName");
    const reason = document.getElementById("reason");
    const compatibilityType = document.getElementById("compatibilityType");
    const resetBtn = document.getElementById("resetBtn");
    const shareBtn = document.getElementById("shareBtn");
    const toast = document.getElementById("toast");
    const pokeBallIcon = document.getElementById("pokeBallIcon");
    const fullscreenBtn = document.getElementById("fullscreenBtn");

    // 전체화면 토글 기능
    fullscreenBtn.addEventListener("click", () => {
      playPopSound();
      if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch((err) => {
          showToast("전체화면을 지원하지 않는 브라우저입니다 😢");
        });
        fullscreenBtn.textContent = "🔳 창모드";
      } else {
        if (document.exitFullscreen) {
          document.exitFullscreen();
        }
        fullscreenBtn.textContent = "🔲 전체화면";
      }
    });

    document.addEventListener("fullscreenchange", () => {
      if (!document.fullscreenElement) {
        fullscreenBtn.textContent = "🔲 전체화면";
      } else {
        fullscreenBtn.textContent = "🔳 창모드";
      }
    });

    // 배경 파티클 애니메이션
    const canvas = document.getElementById("bgCanvas");
    const ctx = canvas.getContext("2d");
    let particles = [];

    function resizeCanvas() {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
    }
    window.addEventListener("resize", resizeCanvas);
    resizeCanvas();

    for (let i = 0; i < 25; i++) {
      particles.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        size: Math.random() * 6 + 3,
        speedY: Math.random() * 0.5 - 0.25,
        speedX: Math.random() * 0.5 - 0.25,
        color: ['#ffeb3b', '#ffc107', '#ff9800', '#fff'][Math.floor(Math.random() * 4)],
        alpha: Math.random() * 0.6 + 0.2
      });
    }

    function animateParticles() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      particles.forEach(p => {
        ctx.fillStyle = p.color;
        ctx.globalAlpha = p.alpha;
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
        ctx.fill();

        p.x += p.speedX;
        p.y += p.speedY;

        if (p.x < 0) p.x = canvas.width;
        if (p.x > canvas.width) p.x = 0;
        if (p.y < 0) p.y = canvas.height;
        if (p.y > canvas.height) p.y = 0;
      });
      requestAnimationFrame(animateParticles);
    }
    animateParticles();

    // 토스트 메시지 함수
    function showToast(msg) {
      toast.textContent = msg;
      toast.classList.remove("opacity-0");
      toast.classList.add("opacity-100");
      setTimeout(() => {
        toast.classList.remove("opacity-100");
        toast.classList.add("opacity-0");
      }, 2000);
    }

    // 볼 아이콘 클릭 인터랙션
    pokeBallIcon.addEventListener("click", () => {
      playSuccessSound();
      showToast("삐비빅! 포켓몬 볼이 반응합니다! ⚡");
    });

    let currentSelectedType = "";

    // MBTI 버튼 클릭 이벤트
    document.querySelectorAll(".mbti-btn").forEach(button => {
      button.addEventListener("click", () => {
        playSuccessSound();
        const type = button.dataset.type;
        currentSelectedType = type;
        const data = pokemonData[type];

        resultMbti.textContent = type + " 유형";
        pokemonEmoji.textContent = data.emoji;
        pokemonName.textContent = data.name;
        reason.innerHTML = data.reason;
        compatibilityType.textContent = data.compatible;

        selection.style.opacity = "0";
        setTimeout(() => {
          selection.style.display = "none";
          result.style.display = "block";
          result.classList.remove("hidden");
        }, 150);
      });
    });

    // 공유하기 버튼
    shareBtn.addEventListener("click", () => {
      playPopSound();
      const data = pokemonData[currentSelectedType];
      const shareText = `[MBTI 포켓몬 테스트] 나의 MBTI(${currentSelectedType}) 소울메이트 포켓몬은 '${data.name}'(${data.emoji})입니다! ✨`;
      
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(shareText).then(() => {
          showToast("결과가 클립보드에 복사되었습니다! 📋");
        }).catch(() => {
          fallbackCopyText(shareText);
        });
      } else {
        fallbackCopyText(shareText);
      }
    });

    function fallbackCopyText(text) {
      const textarea = document.createElement("textarea");
      textarea.value = text;
      document.body.appendChild(textarea);
      textarea.select();
      try {
        document.execCommand('copy');
        showToast("결과가 클립보드에 복사되었습니다! 📋");
      } catch (e) {
        showToast("복사 실패 😢");
      }
      document.body.removeChild(textarea);
    }

    // 다시 고르기 버튼
    resetBtn.addEventListener("click", () => {
      playPopSound();
      result.style.display = "none";
      result.classList.add("hidden");
      selection.style.display = "block";
      setTimeout(() => {
        selection.style.opacity = "1";
      }, 50);
      window.scrollTo({
        top: 0,
        behavior: "smooth"
      });
    });
  </script>
</body>
</html>
