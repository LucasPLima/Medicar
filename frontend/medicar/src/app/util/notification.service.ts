import { Injectable, NgZone } from '@angular/core';
import { MatSnackBar } from '@angular/material/snack-bar';

@Injectable({
  providedIn: 'root'
})
export class NotificationService {

  constructor(private snackBar: MatSnackBar, 
              private zone: NgZone){ }

  private showMessage(textMsg:string, msgType:string):void{
    this.zone.run(()=>{
                        const snackBar = this.snackBar.open(
                          textMsg, "X",{
                            duration: 2000,
                            horizontalPosition:"center",
                            verticalPosition:"top",
                            panelClass:[msgType]
                          }
                        )
                        snackBar.onAction().subscribe(() => {
                          console.log("MACHO")
                          snackBar.dismiss();
                        })
                      }
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
