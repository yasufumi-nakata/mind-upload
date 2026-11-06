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
  var acquisition = document.getElementById('acquisition-calculator');
  if (acquisition) {
    var acquisitionFields = ['volume', 'rate', 'instruments', 'target', 'availability'].map(function (name) {
      return document.getElementById('acq-' + name);
    });
    var acquisitionOutput = document.getElementById('acq-result');
    function formatNumber(value) {
      return value.toLocaleString(ja ? 'ja-JP' : 'en-US', {maximumSignificantDigits: 4});
    }
    function updateAcquisition() {
      acquisitionOutput.replaceChildren();
      if (acquisitionFields.some(function (field) {
        return !field.checkValidity() || !Number.isFinite(Number(field.value));
      })) {
        var error = document.createElement('p');
        error.className = 'error';
        error.textContent = ja ? '体積・速度・年数は正の値，台数は正の整数，追加の稼働割合は0〜1を入力してください。' : 'Use positive volume, rate and years; a positive integer instrument count; and availability between 0 and 1.';
        acquisitionOutput.appendChild(error);
        return;
      }
      var values = acquisitionFields.map(function (field) { return Number(field.value); });
      if (values[4] === 0) {
        var stopped = document.createElement('p');
        stopped.textContent = ja ? '撮像が進みません。有限の所要時間は計算できません。' : 'Imaging makes no progress. No finite duration is available.';
        acquisitionOutput.appendChild(stopped);
        return;
      }
      var years = values[0] / (12 * values[1] * values[2] * values[4]);
      var requiredRate = values[0] / (12 * values[3]);
      var multiplier = years / values[3];
      [
        [ja ? '撮像だけに必要な期間' : 'Imaging time alone', formatNumber(years) + (ja ? ' 年' : ' years')],
        [ja ? '目標期間に必要な実効総速度（休止込み）' : 'Required realized aggregate throughput (including downtime)', formatNumber(requiredRate) + (ja ? ' mm³/月' : ' mm³/month')],
        [ja ? '入力した総速度に対する必要倍率' : 'Required rate / entered aggregate rate', formatNumber(multiplier) + '×']
      ].forEach(function (item) {
        var row = document.createElement('p');
        var value = document.createElement('strong');
        value.textContent = item[1];
        row.appendChild(value);
        row.appendChild(document.createTextNode(item[0]));
        acquisitionOutput.appendChild(row);
      });
    }
    acquisitionFields.forEach(function (field) { field.addEventListener('input', updateAcquisition); });
    Array.from(acquisition.querySelectorAll('[data-acq-preset]')).forEach(function (button) {
      button.addEventListener('click', function () {
        var em = button.dataset.acqPreset === 'em';
        [1200000, em ? 0.3 : 8.8, em ? 200 : 333, 5, 1].forEach(function (value, index) {
          acquisitionFields[index].value = value;
        });
        updateAcquisition();
      });
    });
    updateAcquisition();
  }
})();
