import { Injectable, NgZone } from '@angular/core';
import { MatSnackBar } from '@angular/material/snack-bar';

@Injectable({
  providedIn: 'root'
})
export class NotificationService {

  constructor(private snackBar: MatSnackBar){ }

  private showMessage(textMsg:string, msgType:string):void{
     const snackBarRef =this.snackBar.open(textMsg,'X',{
                            duration: 2000,
                            horizontalPosition:"center",
                            verticalPosition:"top",
                            panelClass:[msgType]
                          }
                        )
    snackBarRef.onAction().subscribe(
      (action)=>snackBarRef.dismiss()
    )
  }

  showSuccessMsg(textMsg:string):void{
    this.showMessage(textMsg, "msg-success")
  }
  showWarningMsg(textMsg:string):void{
    this.showMessage(textMsg, "msg-warning")
  }
  showErrorMsg(textMsg:string):void{
    this.showMessage(textMsg, "msg-error")
  }
}
