(function () {
  'use strict';
  var ja = document.documentElement.lang === 'ja';
  var search = document.getElementById('library-search');
  var category = document.getElementById('library-category');
  if (search && category) {
    var records = Array.from(document.querySelectorAll('.library-record'));
    function filter() {
      var words = search.value.trim().toLocaleLowerCase().split(/\s+/).filter(Boolean);
      var shown = 0;
      records.forEach(function (record) {
        var match = (!category.value || record.dataset.category === category.value) && words.every(function (word) { return record.dataset.search.includes(word); });
        record.hidden = !match;
        if (match) shown++;
      });
      document.getElementById('library-count').textContent = ja ? shown + ' / ' + records.length + ' 件' : shown + ' / ' + records.length + ' records';
      document.getElementById('library-empty').hidden = shown !== 0;
    }
    search.addEventListener('input', filter);
    category.addEventListener('change', filter);
    filter();
  }
  var calculator = document.getElementById('scale-calculator');
  if (calculator) {
    var fields = Array.from(calculator.querySelectorAll('input'));
    function quantity(value, units) {
      var n = 0;
      while (value >= 1000 && n < units.length - 1) { value /= 1000; n++; }
      return value.toLocaleString(ja ? 'ja-JP' : 'en-US', {maximumFractionDigits: 3}) + ' ' + units[n];
    }
    function update() {
      var out = document.getElementById('calc-result');
      out.replaceChildren();
      if (fields.some(function (field) { return !field.checkValidity() || !Number.isFinite(Number(field.value)); })) {
        var error = document.createElement('p'); error.className = 'error';
        error.textContent = ja ? 'すべての欄に範囲内の正の数値を入力してください。' : 'Enter a positive value within the indicated range in every field.';
        out.appendChild(error); return;
      }
      var v = fields.map(function (field) { return Number(field.value); });
      var imageBytes = v[0] * 1e18 / (v[1] * v[2] * v[3]) * v[4];
      var stateBytes = v[5] * v[6];
      var updates = v[5] * v[7];
      [[ja ? '無圧縮画像の量' : 'Raw image size', quantity(imageBytes,['B','kB','MB','GB','TB','PB','EB','ZB'])],
       [ja ? 'シナプス状態のみ' : 'Synapse states only', quantity(stateBytes,['B','kB','MB','GB','TB','PB','EB','ZB'])],
       [ja ? '密な状態更新' : 'Dense state updates', quantity(updates,['/s','k/s','M/s','G/s','T/s','P/s','E/s'])]].forEach(function (item) {
        var p = document.createElement('p'); var strong = document.createElement('strong');
        strong.textContent = item[1]; p.appendChild(strong); p.appendChild(document.createTextNode(item[0])); out.appendChild(p);
      });
    }
    fields.forEach(function (field) { field.addEventListener('input', update); });
    update();
  }
})();
