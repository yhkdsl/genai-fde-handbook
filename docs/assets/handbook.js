/* GenAI FDE Handbook — theme toggle + persisted checklists + progress bars */
(function () {
  'use strict';

  /* ---- theme ---- */
  var KEY_THEME = 'fde:theme';
  var saved = null;
  try { saved = localStorage.getItem(KEY_THEME); } catch (e) {}
  if (saved) document.documentElement.setAttribute('data-theme', saved);

  function currentTheme() {
    var attr = document.documentElement.getAttribute('data-theme');
    if (attr) return attr;
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }

  function wireTheme() {
    var btn = document.getElementById('themeToggle');
    if (!btn) return;
    function paint() { btn.textContent = currentTheme() === 'dark' ? 'LIGHT' : 'DARK'; }
    paint();
    btn.addEventListener('click', function () {
      var next = currentTheme() === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      try { localStorage.setItem(KEY_THEME, next); } catch (e) {}
      paint();
    });
  }

  /* ---- checklists: persist per page, drive progress bars ---- */
  function pageKey() {
    var f = location.pathname.split('/').pop() || 'index';
    return 'fde:done:' + f;
  }

  function loadDone() {
    try { return JSON.parse(localStorage.getItem(pageKey()) || '{}'); }
    catch (e) { return {}; }
  }

  function saveDone(state) {
    try { localStorage.setItem(pageKey(), JSON.stringify(state)); } catch (e) {}
  }

  function updateProgress() {
    document.querySelectorAll('[data-progress-for]').forEach(function (widget) {
      var scopeId = widget.getAttribute('data-progress-for');
      var scope = scopeId === '*' ? document : document.getElementById(scopeId);
      if (!scope) return;
      var boxes = scope.querySelectorAll('.checklist input[type=checkbox]');
      var done = 0;
      boxes.forEach(function (b) { if (b.checked) done++; });
      var pct = boxes.length ? Math.round((done / boxes.length) * 100) : 0;
      var fill = widget.querySelector('.progress-fill');
      var label = widget.querySelector('.progress-label');
      if (fill) fill.style.width = pct + '%';
      if (label) label.textContent = done + ' / ' + boxes.length + ' 완료 · ' + pct + '%';
    });
  }

  function wireChecklists() {
    var state = loadDone();
    var boxes = document.querySelectorAll('.checklist input[type=checkbox]');
    boxes.forEach(function (box, i) {
      var id = box.getAttribute('data-id') || ('i' + i);
      box.setAttribute('data-id', id);
      if (state[id]) box.checked = true;
      box.addEventListener('change', function () {
        var s = loadDone();
        if (box.checked) s[id] = 1; else delete s[id];
        saveDone(s);
        updateProgress();
      });
    });
    updateProgress();
  }

  function init() { wireTheme(); wireChecklists(); }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
