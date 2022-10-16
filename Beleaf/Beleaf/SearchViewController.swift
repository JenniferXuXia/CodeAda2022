//
//  SearchViewController.swift
//  Beleaf
//
//  Created by Sophia Liu on 10/16/22.
//

import UIKit

class SearchViewController: UIViewController {

    @IBOutlet weak var smallestView: UIView!
    @IBOutlet weak var backButton: UIButton!
    @IBOutlet weak var smallll: UIView!
    @IBOutlet weak var dockkView: UIView!
    @IBOutlet weak var biggestView: UIView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        biggestView.layer.cornerRadius = 47
        smallestView.layer.cornerRadius = 33
        dockkView.layer.cornerRadius = 20
        smallll.layer.cornerRadius = 5
        
       
        // Do any additional setup after loading the view.
    }
    

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */

}
