async function run() {
  const MODEL_URL =
    "https://raw.githubusercontent.com/Hrushi11/Sports-Recognition/main/Seq-JS/model.json";
  const model = await tf.loadLayersModel(MODEL_URL);
  console.log(model.summary());
  //   const input = tf.tensor2d([10.0], [1, 1]);
  //   const result = model.predict(input);
  //   alert(result);
}
run();
