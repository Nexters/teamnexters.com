function toScss(results) {
  const [_, ...data] = results[0].result.rawData;

  const colors = {};
  data.forEach((it) => {
    colors[it[0]] = it[1];
  });

  console.log(colors);
}
