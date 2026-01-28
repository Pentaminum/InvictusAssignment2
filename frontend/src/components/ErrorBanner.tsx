type Props = {
    title?: string;
    message: string;
  };
  
  export default function ErrorBanner({ title = "Something went wrong", message }: Props) {
    return (
      <div className="error" role="alert">
        <div className="errorTitle">{title}</div>
        <div className="errorMsg">{message}</div>
      </div>
    );
  }
  