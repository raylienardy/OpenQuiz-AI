import "./LoadingSpinner.css";

export default function LoadingSpinner({ size = 32, color = "#0d6efd" }) {
  const style = {
    width: size,
    height: size,
    borderTopColor: color,
    borderWidth: Math.max(3, size / 10),
  };
  return <div className="spinner" style={style}></div>;
}
